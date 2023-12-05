response = input("File name: ").strip()
temPonto = response.find(".")
partes = response.rsplit(".", 1)

if temPonto != -1:
    extensao = partes[1]
    match extensao:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case "bin":
            print("application/octet-stream")
        case "PDF":
            print("application/pdf")
else: 
    print("application/octet-stream")
        
        