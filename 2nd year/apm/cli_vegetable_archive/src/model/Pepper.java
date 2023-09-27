package model;

public class Pepper implements Vegetable{
    private final float weight;

    public Pepper(float w){
        this.weight = w;
    }

    @Override
    public float getWeight() {
        return this.weight;
    }

    @Override
    public String toString(){
        return "Pepper, weight (kg): "+ this.getWeight();
    }
}
