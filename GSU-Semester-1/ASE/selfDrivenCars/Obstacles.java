package selfDrivenCars;

import simView.*;
import java.lang.*;
import java.awt.*;
import genDevs.plots.*;
import genDevs.modeling.*;
import genDevs.simulation.*;
import GenCol.*;
import java.util.*;

/**
 * <p>Title: </p>
 * <p>Description: </p>
 * <p>Copyright: Copyright (c) 2003</p>
 * <p>Company: </p>
 * @author not attributable
 * @version 1.0
 */

public class Obstacles extends ViewableAtomic{

	double frequencyTime = 10;
	Random ran;
	int jobId=0;

  public Obstacles() {
    this("obstacle", 10);
  }

  public Obstacles(String nm, double opt){
    super(nm);
    frequencyTime = opt;
    //addInport("in");
    addOutport("out");
    ran = new Random();
  }

  public void initialize(){
    super.initialize();
    holdIn("setObstacle", 15);
  }

  public void deltext(double e,message x){
    Continue(e);
    //passivate();
  }

  public void deltint(){
    //passivate();
	  jobId++;
		if (phaseIs("setObstacle")){
			double nextObstacleTime = ran.nextDouble()*frequencyTime;
			holdIn("setObstacle", nextObstacleTime);
		}
  }

  public message out(){
    message m = new message();
    if (phaseIs("setObstacle")) {
      double porcT = 10+10*ran.nextDouble();	
      ObstacleEntity obse = new ObstacleEntity("Obstacle_" + jobId, porcT, 0);
      m.add(makeContent("out", obse));
    }
    return m;
  }


}