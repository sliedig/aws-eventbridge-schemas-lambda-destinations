import pytest

from order_notification_handler import app
from schema.com_aws_orders.ordernotification import AWSEvent
from schema.com_aws_orders.ordernotification import OrderNotification
from schema.com_aws_orders.ordernotification import Marshaller

@pytest.fixture()
def eventBridgeEvent():
    """ Generates EventBridge Event"""

    return {
            "version":"0",
            "id":"7bf73129-1428-4cd3-a780-95db273d1602",
            "detail-type":"Order Notification",
            "source":"com.aws.orders",
            "account":"123456789012",
            "time":"2015-11-11T21:29:54Z",
            "region":"us-east-1",
            "resources":[
              "arn:aws:ec2:us-east-1:123456789012:instance/i-abcd1111"
            ],
            "detail":{
              "{  \"order_id\": 1073459984,  \"shipping_id\": \"34VB5540K83\",  \"currency\": \"USD\",  \"created_at\": \"2019-10-16T16:05:09-04:00\",  \"price\": {    \"total_price\": 24.62,    \"item_price\": 18.99,    \"shipping\": 2.99,    \"taxes\": 2.64  },  \"tax_price\": 2.64,  \"product\": {    \"product_id\": 788032119674292922,    \"title\": \"Encrypt Everything Tshirt\",    \"sku\": \"encrypt-everything-tshirt\",    \"inventory_id\": 23190823132,    \"size\": \"medium\",    \"taxable\": true,    \"image_url\": \"https://img.mystore.test/encrypt-tshirt.jpg\",    \"weight\": 200.0,    \"weight_unit\": \"g\"  },  \"customer\": {    \"name\": \"Alejandro Rosalez\",    \"email\": \"AlejandroRosalez@amazondomains.com\",    \"phone\": \"+1 604 555 0100\"  },  \"shipping_address\": {    \"street\": \"123 Any Street, Any Town, USA\",    \"city\": \"Vancouver\",    \"state\": \"British Columbia\",    \"zip_code\": \"V6B5M1\",    \"country\": \"Canada\"  }}"
            }
    }


def test_lambda_handler(eventBridgeEvent, mocker):

    ret = app.lambda_handler(eventBridgeEvent, "")

    awsEventRet:AWSEvent = Marshaller.unmarshall(ret, AWSEvent)
    detailRet:OrderNotification = awsEventRet.detail

    assert awsEventRet.detail_type.startswith("Order Notification Processed")
