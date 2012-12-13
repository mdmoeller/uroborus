
package abc;

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

class DisplayResult
{
	public static void main(String args[]) throws Exception
	{
		String f1=null;
		int line_number=0;

		if(args.length!=0)
		{
			f1=args[0];
			if(args.length>1)
				line_number=Integer.parseInt(args[1]);
		
		}
		Computation cc=new Computation(f1);
		cc.codeToString();
   
		cc.getCount();
		cc.pfArray();
    
		cc.pfCal();
		cc.statementPassFail();
		cc.getColorValue();
		if(line_number!=0)
		{
    
			cc.createMutantFile(f1, line_number);
		}
    	
		cc.createOutput(f1);    
    
	}
}
