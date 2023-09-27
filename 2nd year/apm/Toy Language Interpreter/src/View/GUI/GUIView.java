package View.GUI;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class GUIView extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception {
        FXMLLoader mainLoader = new FXMLLoader();
        mainLoader.setLocation(getClass().getResource("ProgramRunController.fxml"));
        Parent mainWindow = mainLoader.load();

        ProgramRunController mainWindowController = mainLoader.getController();

        primaryStage.setTitle("WATCH YOUR SELECTED PROGRAM HERE");
        primaryStage.setScene(new Scene(mainWindow, 870, 720));
        primaryStage.show();


        FXMLLoader secondaryLoader = new FXMLLoader();
        secondaryLoader.setLocation(getClass().getResource("ProgramListSelector.fxml"));
        Parent secondaryWindow = secondaryLoader.load();

        ProgramListSelector selectWindowController = secondaryLoader.getController();
        selectWindowController.setProgramController(mainWindowController);

        Stage secondaryStage = new Stage();
        secondaryStage.setTitle("SELECT A PROGRAM YOU WANNA RUN");
        secondaryStage.setScene(new Scene(secondaryWindow, 500, 550));
        secondaryStage.show();
    }


    public static void main(String[] args) {
        launch(args);
    }
}