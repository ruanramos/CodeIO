def bigger_price(limit, data):
    """
        TOP most expensive goods
    """
    # your code here
    values = []
    dics = []
    for item in data:
        values.append(item['price'])
        dics.append(0)

    values.sort()
    for item in data:
        for name, price in item.items():
            if price == values[-1]:
                dics.append({'name': name, 'price': price})
                values.pop()
    
    return dics
