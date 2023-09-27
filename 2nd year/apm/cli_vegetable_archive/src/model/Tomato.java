package model;

public class Tomato implements Vegetable{

    private final float weight;

    public Tomato(float w){
        this.weight = w;
    }

    @Override
    public float getWeight() {
        return this.weight;
    }

    @Override
    public String toString(){
        return "Tomato, weight (kg): "+ this.getWeight();
    }
}
