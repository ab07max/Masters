/*      Copyright 2002 Arizona Board of regents on behalf of
 *                  The University of Arizona
 *                     All Rights Reserved
 *         (USE & RESTRICTION - Please read COPYRIGHT file)
 *
 *  Version    : DEVSJAVA 2.7
 *  Date       : 08-15-02
 */


package selfDrivenCars;

import simView.*;


import genDevs.modeling.*;
import GenCol.*;

public class Junction extends  ViewableAtomic{
 protected double observation_time;
 
 public Junction(String  name,double Observation_time){
  super(name);
   addInport("sensorWatchIn");
  addInport("ariv");
  observation_time = Observation_time;
  addTestInput("ariv",new entity("val"));
  initialize();
 }

 public Junction() {this("junction", 400);}

 public void initialize(){
	 holdIn("active",observation_time);
 }


 public void  deltext(double e,message  x){
  Continue(e);
 }

 public void  deltint(){
  passivate();
 }

 public  message    out( ){
  message  m = new message();
  content  con = makeContent("out",new entity("stop"));
  m.add(con);
  return m;
 }
}
