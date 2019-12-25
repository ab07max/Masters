package selfDrivenCars;

import genDevs.*;
import genDevs.modeling.*;

import java.util.Random;

import GenCol.*;
import simView.ViewableAtomic;


public class SensorDataGenerator extends ViewableAtomic{
	double pedestrianProcessingTime = 3;
	double obstacleProcessingTime = 2;
	entity currentJob=null;
	DEVSQueue jobQ=null;
	int jobId=0;
	Random ran;
	String entity;

	public SensorDataGenerator(){
		this("SensorDataGenerator", 3);
	}

	public SensorDataGenerator(String nm, double ppT){
		super(nm);
		pedestrianProcessingTime = ppT;
		obstacleProcessingTime = ppT * 1.1;
		jobQ = new DEVSQueue();
		currentJob = new entity("NullJob");
		ran = new Random();
		addInport("pedestrianSenseIn");
		addInport("obstacleSenseIn");
		addOutport("out");
		addOutport("out1");
		addTestInput("pedestrianSenseIn",new entity("testPedestrianSense"));
	}

	public void initialize(){
		passivateIn("wait");
	}

	public void deltext(double e,message x){
		Continue(e);
		
		if (phaseIs("wait")){
			for (int i = 0; i < x.getLength(); i++){
				if(messageOnPort(x, "pedestrianSenseIn", i)) {
					currentJob = x.getValOnPort("pedestrianSenseIn", i);
					pedestrianProcessingTime = ((PedestrianEntity)currentJob).procTime;
					holdIn("busy", pedestrianProcessingTime);
				}
				else if(messageOnPort(x, "obstacleSenseIn", i)) {
					currentJob = x.getValOnPort("obstacleSenseIn", i);
					holdIn("busy", obstacleProcessingTime);
				}
			}
		}
		else if (phaseIs("busy")){
			for (int i = 0; i < x.getLength(); i++){
				if (messageOnPort(x, "pedestrianSenseIn", i)) {
					entity job = x.getValOnPort("pedestrianSenseIn", i);
					jobQ.add(job);
				}
				if (messageOnPort(x, "obstacleSenseIn", i)) {
					entity job = x.getValOnPort("obstacleSenseIn", i);
					jobQ.add(job);
				}
			}
		}
//		else if (phaseIs("obstacle detected")){
//			for (int i = 0; i < x.getLength(); i++){
//				if (messageOnPort(x, "obstacleSenseIn", i)) {
//					entity job = x.getValOnPort("obstacleSenseIn", i);
//					jobQ.add(job);
//				}
//			}
//			passivateIn("wait");
//		}
		
	}

	public void   deltint(){
		jobId++;
		if (phaseIs("busy")){
			if(jobQ.size()!=0){
				currentJob=(entity)jobQ.pop();
				if (currentJob.toString().matches("Obstacle_.*")) {
					obstacleProcessingTime = ((ObstacleEntity)currentJob).procTime;
					holdIn("busy", obstacleProcessingTime);
					entity = "obstacle";
				}
				else {
					pedestrianProcessingTime = ((PedestrianEntity)currentJob).procTime;
					holdIn("busy", pedestrianProcessingTime);
					entity = "pedestrian";
				}
			}
			else
				passivateIn("wait");
		}		
	}

	public message out(){
		message m = new message();
		if (phaseIs("busy")) {
			double porcT = 10+10*ran.nextDouble();
			if (entity.equals("pedestrian")) {
				SensorEntity sEnt = new SensorEntity("sensorData_"+jobId,porcT,0);
				m.add(makeContent("out", sEnt));
			}
			else {
				m.add(makeContent("out1", new entity("collisionInformation")));
				//m.add(makeContent("out1", new entity("collisionInformation_"+jobId)));
			}
			//m.add(makeContent("out", currentJob));
		}
//		if (phaseIs("obstacle detected")) {
//			double porcT = 10+10*ran.nextDouble();
//			SensorEntity sEnt = new SensorEntity("obstacleData_"+jobId,porcT,0);
//			m.add(makeContent("out1", sEnt));
//			//m.add(makeContent("out", currentJob));
//		}
		return m;
	}

	public String getTooltipText(){
		  return
		  super.getTooltipText()
		  +"\n"+"Queue Size="+ jobQ.size()
		  +"\n"+"currentJob="+ currentJob.getName();
		  }

}
