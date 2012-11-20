
// package abc;

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
	String f1=null;//, f2=null, f3=null;
	if(args.length!=0)
	{
		f1=args[0];
		/*f2=args[1];
		f3=args[2];*/
	}
    Computation cc=new Computation(f1);
    cc.codeToString();
    //cc.seeCode();
    cc.getCount();
    cc.pfArray();
    //cc.seePFArray();
    cc.pfCal();
    cc.statementPassFail();
    cc.getColorValue();
    cc.createOutput(f1);    
    
}
}




