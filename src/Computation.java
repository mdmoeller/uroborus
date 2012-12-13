import java.io.*;

import java.text.DecimalFormat;
import java.util.*;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Computation 
{

	private String code[];
	private File f,f1,f2;
	private BufferedReader buffered_reader,buffered_reader0,buffered_reader1,buffered_reader2, buffered_reader_count_coverage;
	private List<String> lines;
	private  int count,index, passfail[],pass, fail, statement_passfail[][],col[],pp,ff;
	private FileWriter fstream;
	private BufferedWriter out ;

	private double bright[];
	int blank[];
	private String results[];
       
	public Computation(String file1) throws FileNotFoundException
	{
		String path=("");
		f=new File(path+file1+".py");
		f1=new File(path+file1+"_passfail.txt");  
		f2=new File(path+file1+"_coverage.txt");
		buffered_reader=new BufferedReader(new FileReader(f));
		buffered_reader0=new BufferedReader(new FileReader(f1));  
		buffered_reader1=new BufferedReader(new FileReader(f1));  
		buffered_reader2=new BufferedReader(new FileReader(f2)); 
		buffered_reader_count_coverage=new BufferedReader(new FileReader(f2));
		lines = new ArrayList<String>(); 
        
	}


	//Stores code in String array
	public void codeToString() throws IOException
	{
		String line = null;
		line=buffered_reader.readLine();
		int i=0;
        
        while(line!=null)
        {
        	
        	
        	lines.add(i+1+":"+line);
        	line=buffered_reader.readLine();
        	i++;
        }	
        lines.add(null);
        code=lines.toArray(new String[lines.size()]);
        for(int k=code.length-1;k>0;k--)
        	code[k]=code[k-1];
        code[0]=null;
         
        bright=new double[code.length];
        blank=new int[code.length];
         
        results=new String[code.length];
	}

	//Display code stored in array
	public void seeCode()
	{
		System.out.println("code array:");
        
        int s=0;
        for(int k=1;k<code.length;k++)
        {
        	
        	System.out.println(code[k]);
        	if(code[k]=="	")
        		blank[s++]=k;
        }	
	}

	//Count number of runs i.e. number of entries in passfail file
	public void getCount() throws IOException
	{
		String str=buffered_reader0.readLine();
    
		while(str!=null)
        {
			count++;
            str=buffered_reader0.readLine();    
        }
		buffered_reader0.close(); 
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
        	line1=buffered_reader1.readLine();
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
        
        
	}

	//Display entries of pf array
	public void seePFArray()
	{
        System.out.println("pass/fail array:");
        for(int k=0;k<passfail.length;k++)
        	
        System.out.println(passfail[k]);
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
        
      
        if(pass == 0 || fail == 0) {
            System.out.println("Cannot generate report when no passes or no fails");
            System.exit(1);
        }
        buffered_reader1.close();
      
	}


	/*Count number of times each statement has failed and passed
	 * e.g. if stpf[1][0]=2, then it means statement 1 failed in 2 runs
	 */
	public void statementPassFail() throws IOException
	{
		int count=0;
		String str3=buffered_reader_count_coverage.readLine();
		while(str3!=null) {count++; str3=buffered_reader_count_coverage.readLine();}
		String temp_array[]=new String[count];
		boolean flag;
		temp_array[0]="";
		int r=0;
		statement_passfail=new int[code.length][2];
		String str2=buffered_reader2.readLine();
		int statement_no=0;
		int run_number=0;
    
		while(str2!=null)
        {
    	  	flag=false;
        	
    	  	for(int i=0;i<=r;i++)
        	{		
        		
    	  		if(str2.equals(temp_array[i]))
        		{
        			
        			flag=true;
        			
        			break;
        		}
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
            str2=buffered_reader2.readLine();
        }
      
        	  
        buffered_reader2.close();
        
	}

	//Calculate the color value in % by the given formula
	public void getColorValue()
	{
		col=new int[code.length];
		double result;
		int f;
		int p;
		double percent_pass;
		double percent_fail;
		for(int i=1;i<code.length;i++)
		{
			f=statement_passfail[i][0];
			p=statement_passfail[i][1];
        
       
			double ppassed=((double)p/(double)pass);
			double pfailed=((double)f/(double)fail);
        
			percent_pass=ppassed*100;
			percent_fail=pfailed*100;
         
        
			DecimalFormat twoDForm = new DecimalFormat("#.##");
			percent_pass=Double.valueOf(twoDForm.format(percent_pass));
			percent_fail=Double.valueOf(twoDForm.format(percent_fail));
        
        
			String res="Passed: "+percent_pass+"%; Failed: "+percent_fail+"%";
        
        
			results[i]=res;
        
        
			result=((ppassed)/(ppassed+pfailed))*120;
       
			col[i]=(int)result;
        
			if(ppassed>pfailed)
				bright[i]=ppassed;
			else bright[i]=pfailed;
       
      
		}
    
	}

	public void createMutantFile(String file_name, int line_number) throws IOException
	{
		int sum=0;
		for(int i=1;i<code.length;i++)
		{
			if(i!=line_number)
			sum+=col[i];
		}
		int average=sum/code.length;
		String mutantFileName=file_name+"_colors.txt";
		FileWriter fwriter=new FileWriter(mutantFileName, true);
		BufferedWriter writer = new BufferedWriter(fwriter);
		writer.write(average+"\t"+col[line_number]);
		writer.newLine();

		writer.close();
	}


	public void createOutput(String file_name) throws IOException
	{
    
		CreateHtml.create(code,col, statement_passfail,results, file_name); 
  
    
	}
}
