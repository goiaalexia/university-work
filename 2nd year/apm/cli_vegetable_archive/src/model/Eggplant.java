package model;

public class Eggplant implements Vegetable{
    private final float weight;

    public Eggplant(float w){
        this.weight = w;
    }

    @Override
    public float getWeight() {
        return this.weight;
    }

    @Override
    public String toString(){
        return "Eggplant, weight (kg): "+ this.getWeight();
    }

}
