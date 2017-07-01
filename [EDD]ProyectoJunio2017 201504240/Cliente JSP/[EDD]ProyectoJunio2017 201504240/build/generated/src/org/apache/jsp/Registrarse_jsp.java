package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;

public final class Registrarse_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent {

  private static final JspFactory _jspxFactory = JspFactory.getDefaultFactory();

  private static java.util.List<String> _jspx_dependants;

  private org.glassfish.jsp.api.ResourceInjector _jspx_resourceInjector;

  public java.util.List<String> getDependants() {
    return _jspx_dependants;
  }

  public void _jspService(HttpServletRequest request, HttpServletResponse response)
        throws java.io.IOException, ServletException {

    PageContext pageContext = null;
    HttpSession session = null;
    ServletContext application = null;
    ServletConfig config = null;
    JspWriter out = null;
    Object page = this;
    JspWriter _jspx_out = null;
    PageContext _jspx_page_context = null;

    try {
      response.setContentType("text/html;charset=UTF-8");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;
      _jspx_resourceInjector = (org.glassfish.jsp.api.ResourceInjector) application.getAttribute("com.sun.appserv.jsp.resource.injector");

      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("<!DOCTYPE html>\n");
      out.write("<html lang=\"en\">\n");
      out.write("\n");
      out.write("<head>\n");
      out.write("\n");
      out.write("    <meta charset=\"utf-8\">\n");
      out.write("    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n");
      out.write("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n");
      out.write("    <meta name=\"description\" content=\"\">\n");
      out.write("    <meta name=\"author\" content=\"\">\n");
      out.write("\n");
      out.write("    <title>Registro Usuario</title>\n");
      out.write("\n");
      out.write("    <!-- Bootstrap Core CSS -->\n");
      out.write("    <link href=\"css/bootstrap.min.css\" rel=\"stylesheet\">\n");
      out.write("\n");
      out.write("    <!-- Custom CSS -->\n");
      out.write("    <link href=\"css/landing-page.css\" rel=\"stylesheet\">\n");
      out.write("\n");
      out.write("    <!-- Custom Fonts -->\n");
      out.write("    <link href=\"font-awesome/css/font-awesome.min.css\" rel=\"stylesheet\" type=\"text/css\">\n");
      out.write("    <link href=\"https://fonts.googleapis.com/css?family=Lato:300,400,700,300italic,400italic,700italic\" rel=\"stylesheet\" type=\"text/css\">\n");
      out.write("\n");
      out.write("    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->\n");
      out.write("    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->\n");
      out.write("    <!--[if lt IE 9]>\n");
      out.write("        <script src=\"https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js\"></script>\n");
      out.write("        <script src=\"https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js\"></script>\n");
      out.write("    <![endif]-->\n");
      out.write("\n");
      out.write("</head>\n");
      out.write("\n");
      out.write("<body>\n");
      out.write("    <form>\n");
      out.write("    <!-- Navigation -->\n");
      out.write("    <nav class=\"navbar navbar-default navbar-fixed-top topnav\" role=\"navigation\">\n");
      out.write("        <div class=\"container topnav\">\n");
      out.write("            <!-- Collect the nav links, forms, and other content for toggling -->\n");
      out.write("            <div class=\"collapse navbar-collapse\" id=\"bs-example-navbar-collapse-1\">\n");
      out.write("                <ul class=\"nav navbar-nav navbar-right\">\n");
      out.write("                    <li>\n");
      out.write("                        <a href=\"IniciarSesion.jsp\">Iniciar Sesión </a>\n");
      out.write("                        <a href=\"LecturaArchivoUsuarios.jsp\">Registrar usuarios leyendo un archivo</a>\n");
      out.write("                    </li>\n");
      out.write("                </ul>\n");
      out.write("            </div>\n");
      out.write("            <!-- /.navbar-collapse -->\n");
      out.write("        </div>\n");
      out.write("        <!-- /.container -->\n");
      out.write("    </nav>\n");
      out.write("\n");
      out.write("\n");
      out.write("    <!-- Header -->\n");
      out.write("    <div class=\"intro-header\">\n");
      out.write("        <div class=\"container\">\n");
      out.write("\n");
      out.write("            <div class=\"row\">\n");
      out.write("                <div class=\"col-lg-12\">\n");
      out.write("                    <div class=\"intro-message\">\n");
      out.write("                        <h1>Introduzca sus datos para ser almacenados!!!</h1>\n");
      out.write("                        <h3>Nombre de usuario</h3>\n");
      out.write("                        <span><font color=\"#000000\"><input type=\"text\" name=\"UsuarioNuevo\"></font></input></span><br></br>\n");
      out.write("                        <h3>Contraseña</h3>\n");
      out.write("                        <span><font color=\"#000000\"><input type=\"text\" name=\"ContraNueva\" ></font></input></span><br></br>\n");
      out.write("                        <h3>Confirmar contraseña</h3>\n");
      out.write("                        <span><font color=\"#000000\"><input type=\"text\" name=\"ContraConfirm\" ></font></input></span><br></br>\n");
      out.write("                        <span><font color=\"#000000\"><input type=\"submit\" value=\"Validar\"></input></font></span><br></br>\n");
      out.write("                        ");

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
                       
      out.write("\n");
      out.write("                        <font color=\"#000000\"><p class=\"copyright text-muted small\">Copyright &copy; Your Company 2017. All Rights Reserved</p></font>    \n");
      out.write("                    </div>\n");
      out.write("                </div>\n");
      out.write("            </div>\n");
      out.write("\n");
      out.write("        </div>\n");
      out.write("    </div>\n");
      out.write("                                     \n");
      out.write("    </form>\n");
      out.write("</body>\n");
      out.write("\n");
      out.write("</html>\n");
      out.write("\n");
    } catch (Throwable t) {
      if (!(t instanceof SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          out.clearBuffer();
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
        else throw new ServletException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}
