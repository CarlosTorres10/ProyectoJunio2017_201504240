<%-- 
    Document   : Registrarse
    Created on : 8/05/2017, 01:08:43 AM
    Author     : chato
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Registro Usuario</title>

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
        <div class="container topnav">
            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav navbar-right">
                    <li>
                        <a href="IniciarSesion.jsp">Iniciar Sesión </a>
                        <a href="LecturaArchivoUsuarios.jsp">Registrar usuarios leyendo un archivo</a>
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
                        <h1>Introduzca sus datos para ser almacenados!!!</h1>
                        <h3>Nombre de usuario</h3>
                        <span><font color="#000000"><input type="text" name="UsuarioNuevo"></font></input></span><br></br>
                        <h3>Contraseña</h3>
                        <span><font color="#000000"><input type="text" name="ContraNueva" ></font></input></span><br></br>
                        <h3>Confirmar contraseña</h3>
                        <span><font color="#000000"><input type="text" name="ContraConfirm" ></font></input></span><br></br>
                        <span><font color="#000000"><input type="submit" value="Validar"></input></font></span><br></br>
                        <%
                            java.lang.String UsuarioNuevo=(String) request.getParameter("UsuarioNuevo");
                            java.lang.String ContraNueva=(String) request.getParameter("ContraNueva");
                            java.lang.String ContraConfirm=(String) request.getParameter("ContraConfirm");
                         
                            if (UsuarioNuevo==null && ContraNueva==null && ContraConfirm==null){
                                out.println("<br><font color=\"#000000\">Usuario->"+ UsuarioNuevo +"<<>> Contrasena->"+ ContraNueva + "<<>> Contrasena Confirmar->"+ ContraConfirm + "</font></br>");
                           
                            }
                            else{
                                String conectado;
                                conectado="0";
                                if(ContraNueva.equals(ContraConfirm)){
                                    Clases.ValidarRegistros Registro = new Clases.ValidarRegistros();
                                    if (Registro.ValidarUsuario(UsuarioNuevo, ContraNueva, conectado)==true){
                                       out.println("<br><font color=\"#000000\"><font size=6s>El usuario ya existe intentelo nuevamente!!!</font></font></br>");  
                                    }
                                    else{
                                        
                                        out.println("<br><font color=\"#000000\"><font size=12>Usuario creado con exito!!!</font></font></br>");
                                    }
                                    
                                }
                                else{
                                        out.println("<br><font color=\"#000000\"><font size=8>Las contraseñas no coinciden!!!</font></font></br>");
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

