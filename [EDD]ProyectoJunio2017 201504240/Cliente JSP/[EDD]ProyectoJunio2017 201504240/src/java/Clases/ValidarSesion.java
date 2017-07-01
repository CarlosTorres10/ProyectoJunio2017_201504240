package Clases;

import static Clases.ValidarRegistros.webClient;
import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;
import java.io.IOException;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;
import java.util.logging.Logger;
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author chato
 */
public class ValidarSesion {
    public static OkHttpClient webClient = new OkHttpClient();

    public boolean ValidarLogin(String Usuario,String Password){
        RequestBody formBody = new FormEncodingBuilder()
                .add("Usuario", Usuario)
                .add("Password", Password)
                .build();
        String r= getString("validarLogin",formBody);
        if (r.equals(("TRUE"))){
            return true;
        }
        else{
            return false;
        }
    }
    public boolean ReporteUsuario(){
        RequestBody formBody = new FormEncodingBuilder()
                .add("ReporteUsuario", "")
                .build();
        String r= getString("graficarUsuarios",formBody);
        if (r.equals(("TRUE"))){
            return true;
        }
        else{
            return false;
        }
    }
    
    public boolean ReporteUsuarioConListas(){
        RequestBody formBody = new FormEncodingBuilder()
                .add("ReporteUsuarioConListas", "")
                .build();
        String r= getString("graficarUsuariosConListas",formBody);
        if (r.equals(("TRUE"))){
            return true;
            
        }
        else{
            return false;
        }
    }
 
        private String getString(String metodo, RequestBody formBody) {
        try {
            URL url = new URL("http://127.0.0.1:5000/" + metodo);
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(Clases.ValidarSesion.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(Clases.ValidarSesion.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
    
}


