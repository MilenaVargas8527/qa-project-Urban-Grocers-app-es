import sender_stand_request
import data

def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body

def get_new_user_token():
    user_body = data.user_body
    reponse = sender_stand_request.post_create_new_user(user_body)
    return reponse.json()["authToken"]

def positive_assert(kit_body):
    reponse = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert reponse.status_code == 201
    assert reponse.json()["name"] == kit_body["name"]

def negative_assert_400(kit_body):
    reponse = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert reponse.status_code == 400

#Prueba 1 El número permitido de caracteres (1): kit_body = { "name": "a"}

def test1_create_kit_1_letter_in_the_name_success_reponse():
    current_kit_body = get_kit_body(data.test1_kit_name)
    positive_assert(current_kit_body)

#Prueba 2 El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}

def test2_create_kit_511_letter_in_the_name_success_reponse():
    current_kit_body = get_kit_body(data.test2_kit_name)
    positive_assert(current_kit_body)

#Prueba 3 El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }

def test3_create_kit_0_letter_in_the_name_success_reponse():
    current_kit_body = get_kit_body(data.test3_kit_name)
    negative_assert_400(current_kit_body)

#Prueba 4 El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }

def test4_create_kit_512_letter_in_the_name_success_reponse():
    current_kit_body = get_kit_body(data.test4_kit_name)
    negative_assert_400(current_kit_body)

# Prueba 5 Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }

def test5_create_kit_especial_letter_in_the_name_success_reponse():
    current_kit_body = get_kit_body(data.test5_kit_name)
    positive_assert(current_kit_body)

# Prueba 6 Se permiten espacios: kit_body = { "name": " A Aaa " }

def test6_create_kit_mayus_letter_in_the_name_success_reponse():
    current_kit_body = get_kit_body(data.test6_kit_name)
    positive_assert(current_kit_body)

# Prueba 7 Se permiten números: kit_body = { "name": "123" }

def test7_create_kit_number_in_the_name_success_reponse():
    current_kit_body = get_kit_body(data.test7_kit_name)
    positive_assert(current_kit_body)

# Prueba 8 El parámetro no se pasa en la solicitud: kit_body = { }

def test8_create_kit_whithout_name_parameter():
    current_kit_body =data.kit_body.copy()
    current_kit_body.pop("name")
    negative_assert_400(current_kit_body)

# Prueba 9 Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }

def test9_create_kit_diferentnumber_in_the_name_success_reponse():
    current_kit_body = get_kit_body(data.test9_kit_name)
    negative_assert_400(current_kit_body)








