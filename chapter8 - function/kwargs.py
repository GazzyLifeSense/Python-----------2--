def save_car(factory, id, **car_info):
    car = {factory:factory, id:id}
    if car_info.get('color'):
        car['color'] = car_info['color']
    if car_info.get('tow_package'):
        car['tow_package'] = car_info['tow_package']
    return car

print(save_car('Ford', 'Focus', color='blue', tow_package=True))
            