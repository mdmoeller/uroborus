/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

// package abc;

import java.io.*;

import java.util.*;
import java.util.logging.Level;
import java.util.logging.Logger;



/**
 *
 
 */
public class CodeChecker {

    private String code[];
    private File f,f1,f2;
    private BufferedReader br,br0,br1,br2;
    private List<String> lines;
    private int count,index, pf[],pass, fail, stpf[][],col[],pp,ff;
    private FileWriter fstream;
    private BufferedWriter out ;



    public CodeChecker() throws FileNotFoundException
    {
        f=new File("/Users/Twisha/Documents/SE/Project/uroborus/ex/euclid/euclid.py");
        f1=new File("/Users/Twisha/Documents/SE/Project/reprojectrequirements/euclid_passfail.txt");  
        f2=new File("/Users/Twisha/Documents/SE/Project/reprojectrequirements/euclid_coverage.txt");
        br=new BufferedReader(new FileReader(f));
        br0=new BufferedReader(new FileReader(f1));  
        br1=new BufferedReader(new FileReader(f1));  
        br2=new BufferedReader(new FileReader(f2));  
        lines = new ArrayList<String>();   


    }


    public void codeToString() throws IOException
    {
        String line = null;

        for(int i=0;i<25;i++)
        {
            line=br.readLine();
            if(line != null)// && line.length()>1 && line.charAt(0)!='#')
                lines.add(line);


        }	
        lines.add(null);
        code=lines.toArray(new String[lines.size()]);
        for(int k=code.length-1;k>0;k--)
            code[k]=code[k-1];
        code[0]=null;
    }

    public void seeCode()
    {
        System.out.println("code array:");


        for(int k=1;k<code.length;k++)
            System.out.println(code[k]);
    }

    public void getCount() throws IOException
    {
        String str=br0.readLine();

        while(str!=null)
        {
            count++;
            str=br0.readLine();    
        }
        br0.close(); 
    }

    public void pfArray() throws IOException
    {
        char r;
        pf=new int[count];
        int w=0;

        String line1 = null;

        for(int i=0;i<pf.length;i++)
        {
            line1=br1.readLine();
            if(line1 != null) 
            {	
                for(int z=0;z<line1.length();z++)
                    if((r=line1.charAt(z))!=' ')
                    {

                        index=Integer.parseInt(String.valueOf(r));

                        break;
                    }	



                for(int z=w+1;z<line1.length();z++)
                    if((r=line1.charAt(z))=='0' || (r=line1.charAt(z))=='1')
                    {

                        int t=Integer.parseInt(String.valueOf(r));

                        pf[index]=t;

                        break;
                    }


            }

        }	


        System.out.println();

    }

    public void seePFArray()
    {
        System.out.println("pass/fail array:");
        for(int k=0;k<pf.length;k++)

            System.out.println(pf[k]);
    }

    public void pfCal() throws IOException
    {
        for(int k=0;k<pf.length;k++)
        {
            if(pf[k]==0)
                fail++;
            else pass++;
        }

        System.out.println("Passes="+pass+"   Fails="+fail);
        br1.close();
        System.out.println();

    }

    public void statementPassFail() throws IOException
    {
        stpf=new int[code.length][2];
        String str2=br2.readLine();
        int statement_no=0;
        int n=0;

        while(str2!=null)
        {
            String delimiter = "	";
            String s[];
            s = str2.split(delimiter);
            statement_no=Integer.parseInt(s[0]);
            n=Integer.parseInt(s[1]);

            if(pf[n]==0)
                stpf[statement_no][0]++;
            else
                stpf[statement_no][1]++;
            str2=br2.readLine();
        }

        for(int k=1;k<code.length;k++)
        {
            for(int m=0;m<2;m++)
                System.out.print(stpf[k][m]+"   ");
            System.out.println();

        }

        br2.close();

    }


    public void getColorValue()
    {
        col=new int[code.length];
        float result;
        float fff;
        float ppp;
        for(int i=1;i<code.length;i++)
        {
            fff=stpf[i][0];
            ppp=stpf[i][1];
            result=((ppp/pass)/(ppp/pass+fff/fail))*120;
            col[i]=(int)result;

        }

    }

    public void createOutput() throws IOException
    {

        CreateHtml.create(code,col);
        /*fstream = new FileWriter("Oo.htm");
          out = new BufferedWriter(fstream);

          out.write("<html><head><title>DATA</title></head>");
          out.write("<body>");
          out.write("<h1>Welcome<h1>");

          String str=null;
          String shade=null;
          String red="red";
          for( int i=1;i<code.length;i++)
          {
          System.out.println(i);
          str=code[i];
        //shade=RangeColor.htmlColor(col[i]);
        //out.write("<font color='"+red+"'>"+str+"</font><br/>");
        //out.write("<font color='red'>"+str+"</font><br/>");
        out.write("<font color='yellow'>Yellow</font><br>");
        System.out.println("red");
          }

          out.write("</body></html>");

        //createHtml ch=new createHtml();
        //CreateHtml.createHtml(code);
         * 
         */
    }












}
class Computation
{
    public static void main(String args[]) throws Exception
    {
        CodeChecker cc=new CodeChecker();
        cc.codeToString();
        cc.seeCode();
        cc.getCount();
        cc.pfArray();
        cc.seePFArray();
        cc.pfCal();
        cc.statementPassFail();
        cc.getColorValue();
        cc.createOutput();    

    }
}
