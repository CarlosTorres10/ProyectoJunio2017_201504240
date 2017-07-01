package Clases;

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author chato
 */
public class ValidarRegistros {
    public static OkHttpClient webClient = new OkHttpClient();
    
    public boolean ValidarUsuario(String Usuario, String Contrasena, String Conectado){
            if (BuscarUsuario(Usuario)==true){
                return true;
            }
            else{
                RequestBody formBody = new FormEncodingBuilder()
                    .add("Usuario", Usuario)
                    .add("Password", Contrasena)
                    .add("Conectado", Conectado)
                    .build();
                String r = getString("insertarEnABB", formBody); 
                System.out.println(r + "---");
                return false;
            }
    }
         
    public boolean BuscarUsuario(String Usuario){
        RequestBody formBody = new FormEncodingBuilder()
                .add("Usuario", Usuario)
                .build();
        String r= getString("buscarEnABB",formBody);
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
            java.util.logging.Logger.getLogger(Clases.ValidarRegistros.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(Clases.ValidarRegistros.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
    
    
    
}
    

