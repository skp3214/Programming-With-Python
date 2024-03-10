http_status=404

match http_status:
    case 200 | 201:
        print("Sucess")
    case 404:
        print("not found")
    case _:
        print("Unkonown")