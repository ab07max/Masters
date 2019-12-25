package selfDrivenCars;

import genDevs.modeling.*;

import java.util.Random;

import GenCol.*;
import simView.ViewableAtomic;


public class ControlSystem extends ViewableAtomic{
	double sensorProcessingTime = 3;
	double obstacleProcessingTime = 1.1 * sensorProcessingTime;
	Random ran;
	entity currentJob=null;
	DEVSQueue jobQ=null;
	String entity;

	public ControlSystem(){
		this("IntelligenceSystem", 3);
	}

	public ControlSystem(String nm, double spT){
		super(nm);
		sensorProcessingTime = spT;
		jobQ = new DEVSQueue();
		currentJob = new entity("NullJob");
		addInport("sensorDataIn");
		addOutport("brake");
		addOutport("accelerate");
		addOutport("air bag");
		addTestInput("sensorDataIn", new entity("testSensor"));	
	}

	public void initialize(){
		passivateIn("wait");
	}

	public void deltext(double e,message x){
		Continue(e);
		
		if (phaseIs("wait")){
			for (int i = 0; i < x.getLength(); i++){
				currentJob = x.getValOnPort("sensorDataIn", i);
				sensorProcessingTime = ((SensorEntity)currentJob).procTime;
				holdIn("busy", sensorProcessingTime);
			}
		}
		else if (phaseIs("busy")){
			for (int i = 0; i < x.getLength(); i++){
				if (messageOnPort(x, "sensorDataIn", i)) {
					entity job = x.getValOnPort("sensorDataIn", i);
					jobQ.add(job);
				}
			}
		}
	}

	public void   deltint(){
		if (phaseIs("busy")){
			if(jobQ.size()!=0){
				currentJob=(entity)jobQ.pop();
				if (currentJob.toString().matches("collision.*")) {
					//obstacleProcessingTime = ((ObstacleEntity)currentJob).procTime;
					holdIn("busy", obstacleProcessingTime);
					entity = "obstacle";
				}
				else {
					sensorProcessingTime = ((SensorEntity)currentJob).procTime;
					holdIn("busy", sensorProcessingTime);
					entity = "sensor";
				}
				
				
			}
			else {
				//passivateIn("wait");
				double accelerateTime = ran.nextDouble()*10;
				holdIn("wait", accelerateTime);
			}
		}		
	}

	public message out(){
		message m = new message();
		if (phaseIs("busy")) {
			if(entity.equals("sensor"))
				m.add(makeContent("brake", new entity("Stop_" + currentJob)));
			else {
				m.add(makeContent("air bag", currentJob));
				//m.add(makeContent("brake", new entity("Stop_" + currentJob)));
			}
		}
		else
			m.add(makeContent("accelerate", new entity("Go")));
		return m;
	}

	public String getTooltipText(){
		  return
		  super.getTooltipText()
		  +"\n"+"Queue Size="+ jobQ.size()
		  +"\n"+"currentJob="+ currentJob.getName();
		  }

}
