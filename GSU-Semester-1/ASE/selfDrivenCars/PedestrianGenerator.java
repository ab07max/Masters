package selfDrivenCars;

import java.util.Random;

import genDevs.modeling.*;
import simView.ViewableAtomic;


public class PedestrianGenerator extends ViewableAtomic{
	double frequencyTime = 10;
	Random ran;
	int jobId=0;
	public PedestrianGenerator(){
		this("PedestrianGenerator", 10);
	}

	public PedestrianGenerator(String nm, double ppT){
		super(nm);
		frequencyTime = ppT;
		addOutport("out");
		ran = new Random();
	}

	public void initialize(){
		holdIn("active", 5);
	}

	public void deltext(double e,message x){
		Continue(e);
	}

	public void   deltint(){
		jobId++;
		if (phaseIs("active")){
			double nextPedestrianTime = ran.nextDouble()*frequencyTime;
			holdIn("active", nextPedestrianTime);
		}
	}

	public message out(){
		message m = new message();
		if (phaseIs("active")){
			//double porcT = 10+10*ran.nextDouble();
			int distance = ran.nextInt(1000);
			double porcT;
			
			//If the distance is more than 300, the car is decently far
			//Otherwise it is near. We calculate the time accordingly.
			if (distance > 300) {
				porcT = distance / 100;
			}
			else {
				porcT = distance / 50;
			}
			
			PedestrianEntity pEnt = new PedestrianEntity("pedestrian_"+jobId+ "_" + distance,porcT,0);
			m.add(makeContent("out", pEnt));
			//m.add(makeContent("out", new entity("car_"+jobId)));
		}
		return m;
	}
}
