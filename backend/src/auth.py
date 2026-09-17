from fastapi import Header, HTTPException, Depends
from database import supabase


def get_token(authorization: str | None = Header(default=None)):
    print("AUTHORIZATION RECIBIDO:", authorization)

    if not authorization:
        raise HTTPException(status_code=401, detail="No estás autenticado")

    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token inválido")

    return authorization.replace("Bearer ", "")


def get_current_user(token: str = Depends(get_token)):
    print("TOKEN RECIBIDO:", token)

    try:
        response = supabase.auth.get_user(token)

        print("USUARIO SUPABASE:", response.user)

        if not response.user:
            raise HTTPException(status_code=401, detail="Usuario no válido")

        return response.user

    except Exception as error:
        print("ERROR VALIDANDO TOKEN:", error)

        raise HTTPException(status_code=401, detail="Token inválido o expirado")
