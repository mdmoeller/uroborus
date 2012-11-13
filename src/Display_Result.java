package abc;

import java.io.*;

import java.util.*;
import java.util.logging.Level;
import java.util.logging.Logger;




public class Display_Result {

    private String code[];
private File file0,f1,file2;
private BufferedReader buffered_reader_code,buffered_reader_passfail,buffered_reader_pf,buffered_reader_coverage;
private List<String> lines;
private  int count,index, passfail[],pass, fail, statement_passfail[][],color[];
private FileWriter fstream;
private BufferedWriter out ;

private double bright[];
int blank[];
       


public Display_Result(String file1) throws FileNotFoundException
{
   String path=("");
	file0=new File(path+file1+".py");
    f1=new File(path+file1+"_passfail.txt");  
    file2=new File(path+file1+"_coverage.txt");
    buffered_reader_code=new BufferedReader(new FileReader(file0));
    buffered_reader_passfail=new BufferedReader(new FileReader(f1));  
    buffered_reader_pf=new BufferedReader(new FileReader(f1));  
    buffered_reader_coverage=new BufferedReader(new FileReader(file2));  
    lines = new ArrayList<String>(); 
        
}


//Stores code in String array
public void codeToString() throws IOException
{
      String line = null;
      line=buffered_reader_code.readLine();
      int i=0;
        
        while(line!=null)
        {
        	
        	lines.add(i+1+":	"+line);
        	line=buffered_reader_code.readLine();
        	i++;
        }	
        lines.add(null);
        code=lines.toArray(new String[lines.size()]);
        for(int k=code.length-1;k>0;k--)
        	code[k]=code[k-1];
         code[0]=null;
         
         bright=new double[code.length];
         blank=new int[code.length];
}


//Count number of runs i.e. number of entries in passfail file
public void getCount() throws IOException
{
    String str=buffered_reader_passfail.readLine();
    
    while(str!=null)
        {
        	count++;
                str=buffered_reader_passfail.readLine();    
        }
      buffered_reader_passfail.close(); 
}

/*Store pass/fail values of each run in pf array indexed by run number
 * e.g. If pf[1]=0 then it means run 1 has failed
 */
public void pfArray() throws IOException
{
    char r;
    passfail=new int[count];
    int w=0;
    
     String line1 = null;
        
        for(int i=0;i<passfail.length;i++)
        {
        	line1=buffered_reader_pf.readLine();
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
        			
        			passfail[index]=t;
        			
        			break;
        		}
        		
        	
        	}
        	
        }	
        
      
        System.out.println();
        
}



//Count total number of passes and fails of all runs
public void pfCal() throws IOException
{
     for(int k=0;k<passfail.length;k++)
        {
        	if(passfail[k]==0)
        		fail++;
        	else pass++;
        }
        
        
        buffered_reader_pf.close();
       
        
}


/*Count number of times each statement has failed and passed
 * e.g. if stpf[1][0]=2, then it means statement 1 failed in 2 runs
 */
public void statementPassFail() throws IOException
{
    String temp_array[]=new String[100];
    boolean flag=false;
    temp_array[0]="";
    int r=0;
	statement_passfail=new int[code.length][2];
    String str2=buffered_reader_coverage.readLine();
    int statement_no=0;
    int run_number=0;
    
      while(str2!=null)
        {
        	for(int i=0;i<=r;i++)
        		
        		if(str2.equals(temp_array[i]))
        		{
        			
        			flag=true;
        			break;
        		}
        		
        		if(!flag)
        		{
        			temp_array[r++]=str2;
        			String delimiter = "	";
        			String s[];
        			s = str2.split(delimiter);
        			statement_no=Integer.parseInt(s[0]);
        			
        			run_number=Integer.parseInt(s[1]);
        			
    			
        			if(passfail[run_number]==0)
                            statement_passfail[statement_no][0]++;
        			else
                            statement_passfail[statement_no][1]++;
        		}	
                str2=buffered_reader_coverage.readLine();
        }
      
       
        
        buffered_reader_coverage.close();
        
}

//Calculate the color value in % by the given formula
public void getColorValue()
{
    color=new int[code.length];
    double result;
    float f;
    float p;
    for(int i=1;i<code.length;i++)
    {
       f=statement_passfail[i][0];
        p=statement_passfail[i][1];
        
        double ppassed=(p/pass);
        double pfailed=(f/fail);
        
        
        
       result=((ppassed)/(ppassed+pfailed))*120;
       
        color[i]=(int)result;
       if(ppassed>pfailed)
       bright[i]=ppassed;
       else bright[i]=pfailed;
       
       
        
    }
    
}

//
public void createOutput() throws IOException
{
    
    CreateHtml.create(code,color, statement_passfail,bright);
  
           
            
}
    











}
class Computations
{
public static void main(String args[]) throws Exception
{
	String f1=null;
	if(args.length!=0)
	
		f1=args[0];
		
    DisplayResult cc=new DisplayResult(f1);
    cc.codeToString();
    
    cc.getCount();
    cc.pfArray();
    
    cc.pfCal();
    cc.statementPassFail();
    cc.getColorValue();
    cc.createOutput();    
    
}
}