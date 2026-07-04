from flask import Blueprint
from flask import jsonify
from flask import request

from flask_jwt_extended import jwt_required

from services.payment_service import PaymentService

payment_bp = Blueprint("payment",__name__)


@payment_bp.route("/",methods=["POST"])
@jwt_required()
def payment():

    data=request.json

    response,status=PaymentService.make_payment(

        data["order_id"],

        data["payment_method"]

    )

    return jsonify(response),status
