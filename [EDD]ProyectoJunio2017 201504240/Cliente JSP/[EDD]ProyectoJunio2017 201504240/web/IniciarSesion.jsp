<%-- 
    Document   : PaginaPrincipal
    Created on : 8/05/2017, 01:07:17 AM
    Author     : chato
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@page session="true"%>
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Iniciar sesion</title>

    <!-- Bootstrap Core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="css/landing-page.css" rel="stylesheet">

    <!-- Custom Fonts -->
    <link href="font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Lato:300,400,700,300italic,400italic,700italic" rel="stylesheet" type="text/css">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

</head>

<body>
    <form>

    <!-- Navigation -->
    <nav class="navbar navbar-default navbar-fixed-top topnav" role="navigation">
            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav navbar-right">
                    <li>
                        <a href="Registrarse.jsp">Registrarse</a>
                        <a href="ArchivoJuegos.jsp">Leer Archivo de Juegos Realizados</a>
                    </li>
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container -->
    </nav>

    <!-- Header -->
    <div class="intro-header">
        <div class="container">

            <div class="row">
                <div class="col-lg-12">
                    <div class="intro-message">
                        <h1>Inicie sesión!!!</h1>
                        <h3>Usuario</h3>
                        <span><font color="#000000"><input type="text" name="Usuario" size="35"></font></input></span><br></br>
                        <h3>Contraseña</h3>
                        <span><font color="#000000"><input type="text" name="Contrasena" size="35"></font></input></span><br></br>
                        <span><font color="#000000"><input type="submit" value="Verificar"></input></font></span><br></br>
                        <%
                            java.lang.String NombreUsuario=(String) request.getParameter("Usuario");
                            java.lang.String Contrasena=(String) request.getParameter("Contrasena");
                            HttpSession VariableSesion = request.getSession();
                            VariableSesion.setAttribute("NombreUsuario",NombreUsuario);
                            if (NombreUsuario == null && Contrasena == null){
                                out.println("<br><font color=\"#000000\">Rellene todos los campos!!!</font></br>");
                            }
                            else{
                                Clases.ValidarSesion Login = new Clases.ValidarSesion();
                                out.println("<br><font color=\"#000000\">Usuario->"+ NombreUsuario +"<<>> Contrasena->"+ Contrasena + "</font></br>");
                                if (Login.ValidarLogin(NombreUsuario, Contrasena)== true){
                                    
                                    response.sendRedirect("SesionIniciada.jsp");
                                    
                                }
                                else{
                                    out.println("<br><font color=\"#000000\"><font size=4>El usuario no existe o los datos estan incorrectos, verifiquelos!!!</font></br>");
                                    
                                }
                            }
                           
                        %>
                        <font color="#000000"><p class="copyright text-muted small">Copyright &copy; Your Company 2017. All Rights Reserved</p></font>    
                    </div>
                </div>
            </div>

        </div>
    </div>
    </form>
    
</body>

</html>

