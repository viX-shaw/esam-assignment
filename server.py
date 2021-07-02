from helpers import get_delivery_charge

from fastapi import FastAPI, Body
from models import OfferTypes,Order,OrderTotal

app = FastAPI()

@app.post("/get_order_total", response_model=OrderTotal)
def get_order_total(order: Order = Body(...)):
    order_total = 0
    discount = 0
    
    #Calculating total order amount without offer
    for entry in order.order_items:
        order_total += entry.quantity * entry.price
    delivery_charge = get_delivery_charge(order.distance)
    order_total += delivery_charge

    if order.offer is not None: # Check, since offers are optional
        if order.offer.offer_type == OfferTypes.FLAT:
            # Discount cannot be greater than total order amount without offer
            discount = min(order.offer.offer_val, order_total)
        if order.offer.offer_type == OfferTypes.DELIVERY:
            discount = delivery_charge

    order_total = order_total - discount
    return {'order_total': order_total}


