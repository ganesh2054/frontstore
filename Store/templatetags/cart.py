from django import template

register = template.Library()

@register.filter(name='cart_quantity')
def cart_quantity(cart):
  return sum(cart.values())

@register.filter(name='productwise_cart_quantity')
def productwise_cart_quantity(product,cart):
    keys=cart.keys()
    for id in keys:
        if int(id)==product.id:
            return cart.get(id)
    return 0

@register.filter(name='price_total')
def price_total(product,cart):
    return product.unit_price*productwise_cart_quantity(product,cart)
@register.filter(name='total_cart_price')
def total_cart_price(product,cart):
    sum=0
    for p in product:
        sum+=price_total(p,cart)
        print('sum is ',sum)

    return sum


    
          
   
  