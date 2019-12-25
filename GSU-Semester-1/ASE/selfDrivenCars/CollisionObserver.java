package selfDrivenCars;

import simView.*;
import java.lang.*;
import genDevs.modeling.*;
import genDevs.simulation.*;
import GenCol.*;

/**
 * <p>Title: </p>
 * <p>Description: </p>
 * <p>Copyright: Copyright (c) 2003</p>
 * <p>Company: </p>
 * @author not attributable
 * @version 1.0
 */

public class CollisionObserver extends ViewableAtomic{

  protected int count;
  protected double clock;
  double infProcessingTime = 20;
  entity currentJob = null;
  DEVSQueue jobQ = null;
  
  public CollisionObserver(String  name,double Observation_time){
	  super(name);
	  addInport("in");
	    addOutport("out");
	  infProcessingTime = Observation_time;
	  jobQ = new DEVSQueue();
	  currentJob = new entity("NullJob");
	  addTestInput("in",new entity("val"));
	  initialize();
	 }

  public CollisionObserver() {
    this("Collision");
  }

  public CollisionObserver(String nm) {
    super(nm);
    
  }

  public void initialize(){
    clock = 0;
    count = 0;
    super.initialize();
    passivateIn("wait");
  }

  public void  deltext(double e,message x){
    clock = clock + e;
    Continue(e);

//    for (int i=0; i< x.getLength();i++){
//      if (messageOnPort(x, "in", i)) {
//        entity en = x.getValOnPort("in", i);
//        if (en.eq("true")) {
//          count = count + 1;
//          holdIn("counting", 0);
//        }
//      }
//    }
    
    if (phaseIs("wait")){
		for (int i = 0; i < x.getLength(); i++){
			currentJob = x.getValOnPort("in", i);
			holdIn("busy", infProcessingTime);
		}
	}
	else if (phaseIs("busy")){
		for (int i = 0; i < x.getLength(); i++){
			if (messageOnPort(x, "in", i)) {
				entity job = x.getValOnPort("in", i);
				jobQ.add(job);
			}
		}
	}


  }

  public void  deltint( ){
    clock = clock + sigma;
    if (phaseIs("busy")){
		if(jobQ.size()!=0){
			currentJob=(entity)jobQ.pop();
			holdIn("busy", infProcessingTime);
		}
		else
			passivateIn("wait");
	}	
  }

  public message  out( ){
    message  m = new message();

    if (phaseIs("busy")) {
        m.add(makeContent("out",  currentJob));
    }
    return m;
  }

  public void showState(){
    super.showState();
  }

}