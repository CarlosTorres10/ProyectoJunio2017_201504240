/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Clases;

import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.Response;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.logging.Level;

/**
 *
 * @author chato
 */
public class path {
    public static OkHttpClient webClient = new OkHttpClient();
    public String [ ] lista;
 public ArrayList<String> listaUrls = new ArrayList<>();
 
 
    public void carpeta(String Usuario, String Carpeta) {
        System.out.println("Esta es la carpeta "+Carpeta);
        String r = getString("obtenerCarpetas/" + Usuario + "/" + Carpeta);
        lista = r.split("<Branch |<Leaf |> |, |>");
        for (String lista1 : lista) {
            String temp = lista1 + "#";
            //    obtenerCarpetas(Usuario, lista[i]);
            if(!"#".equals(temp)){
                System.out.println("--" + temp);
                listaUrls.add(lista1);
                carpeta1(Usuario,lista1);
            }
        }
    }
    public void carpeta1(String Usuario, String Carpeta) {
        System.out.println("Carp "+Carpeta);
        String r = getString("obtenerCarpetas/" + Usuario + "/" + Carpeta);
        System.out.println("URL "+ "obtenerCarpetas/" + Usuario + "/" + Carpeta );
        System.out.println(r);
        lista = r.split("<Branch |<Leaf |> |, |>|None");
        for (String lista1 : lista) {
            String temp =  Carpeta+"/"+ lista1 + "#";
            String temp1 = Carpeta+","+lista1;
            if(!"#".equals(temp)){
                if(temp == null ? Carpeta+"/#" != null : !temp.equals(Carpeta+"/#")){
                    System.out.println("---" + temp);
                listaUrls.add(Carpeta.replace(",", "/")+"/"+lista1);
                carpeta1(Usuario,temp1);
                }
                
            }
        }
    }
    public static String getString(String metodo){
     try {
            URL url = new URL("http://127.0.0.1:8000/" + metodo);
            Request request = new Request.Builder().url(url).get().build();
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
