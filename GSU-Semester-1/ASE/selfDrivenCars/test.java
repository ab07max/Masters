package selfDrivenCars;



import genDevs.modeling.*;
import genDevs.simulation.*;


public class test{

protected static digraph testDig;

  public test(){}

  public static void main(String[ ] args)
  {
      testDig = new SelfDrivingSystem();
      coordinator cs = new coordinator(testDig);

//      TunableCoordinator cs = new TunableCoordinator(testDig);
//      cs.setTimeScale(0.1);

      cs.initialize();
      cs.simulate(50000);
  }
}
