/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Clases;
import static Clases.ValidarRegistros.webClient;
import static Clases.ValidarSesion.webClient;
import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Scanner;

/**
 *
 * @author chato
 */
public class ArchivoUsuarios {
    public static OkHttpClient webClient = new OkHttpClient();
    static String xStrPath;
    static String[] NombreUsuarios,Passwords,ValorConexion;
    static int CantidadFilas;
    
    public boolean LeerArchivo(String RutaArchivo) throws FileNotFoundException{
        Scanner scanIn=null;
        Scanner scanIn2=null;
        int ContadorFilas=0;
        int Fila=0;
        String InputLine="";
        String InputLine2="";
        String XfileLocation;
        XfileLocation=RutaArchivo;
        
        try{
            //El primer while es para verificar la cantidad de lineas que hay.
            scanIn=new Scanner(new BufferedReader(new FileReader(XfileLocation)));
            while (scanIn.hasNextLine()){
                InputLine=scanIn.nextLine();
                ContadorFilas++;
            }
            
            //Asignacion de tamañano de los vectores segun la cantidad de lineas.
            NombreUsuarios = new String[ContadorFilas];
            Passwords=new String[ContadorFilas];
            ValorConexion= new String[ContadorFilas];
            CantidadFilas=NombreUsuarios.length;
            
            //Lectura del archivo nuevamente para llenar los vectores
            scanIn2=new Scanner(new BufferedReader(new FileReader(XfileLocation)));
            while (scanIn2.hasNextLine()){
                InputLine2=scanIn2.nextLine();
                String[] InArray2 =InputLine2.split(",");
                for (int Columna = 0; Columna < InArray2.length; Columna++) {
                
                    if (Columna==0){
                        NombreUsuarios[Fila]=(InArray2[Columna]);
                        //System.out.println(NombreUsuarios[Fila]);
                    }
                    if (Columna==1){
                        Passwords[Fila]=(InArray2[Columna]);
                        //System.out.println(Passwords[Fila]);
                    }
                    if (Columna==2){
                        ValorConexion[Fila]=(InArray2[Columna]);
                        //System.out.println(ValorConexion[Fila]);
                    }
                }
                Fila++;
            } 
            return true;
            
        } catch (Exception e){
            //System.out.println("problemas con el archivo");
            return false;
        }
        
    }
    
    
    
    public boolean IngresarUsuarios(String Ruta) throws FileNotFoundException{
        if (LeerArchivo(Ruta)==true){
            System.out.println("Datos de los usuarios");
            for (int Fila = 1; Fila < CantidadFilas; Fila++) {
                System.out.println(NombreUsuarios[Fila]+" "+Passwords[Fila]+" "+ValorConexion[Fila]);
                RequestBody formBody = new FormEncodingBuilder()
                    .add("Usuario", NombreUsuarios[Fila])
                    .add("Password", Passwords[Fila])
                    .add("Conectado", ValorConexion[Fila])
                    .build();
                String r = getString("insertarEnABB", formBody); 
                System.out.println(r + "---");
            }
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
            java.util.logging.Logger.getLogger(Clases.ArchivoUsuarios.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(Clases.ArchivoUsuarios.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
    
    
    
}
