from controllers import LoginUserControllers, RegistroUserControllers, InicioSesionUserControllers, InicioUserControllers, CategoriasGranosUserControllers, CategoriasCarnesUserControllers, CategoriasVerdurasUserControllers


user = {
    #"login_user": "/api/v01/user/login", "login_user_controllers": LoginUserControllers.as_view("login_api"),
    
    "registro_user": "/api/v01/user/registro", "registro_user_controllers": RegistroUserControllers.as_view("registro_api"),
    "inicio-sesion_user": "/api/v01/user/inicio-sesion", "inicio-sesion_user_controllers": InicioSesionUserControllers.as_view("inicio-sesion_api"),

    "inicio_user": "/api/v01/user/inicio", "inicio_user_controllers": InicioUserControllers.as_view("inicio_api"),
    "categoriasgranos_user": "/api/v01/user/categoriasgranos", "categoriasgranos_user_controllers": CategoriasGranosUserControllers.as_view("categoriasgranos_api"),
    "categoriascarnes_user": "/api/v01/user/categoriascarnes", "categoriascarnes_user_controllers": CategoriasCarnesUserControllers.as_view("categoriascarnes_api"),
    "categoriasverduras_user": "/api/v01/user/categoriasverduras", "categoriasverduras_user_controllers": CategoriasVerdurasUserControllers.as_view("categoriasverduras_api"),

}

