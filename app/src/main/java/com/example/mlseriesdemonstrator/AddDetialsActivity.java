package com.example.mlseriesdemonstrator;

import android.content.SharedPreferences;
import android.os.Bundle;

import com.example.mlseriesdemonstrator.helpers.vision.drowsiness.FaceDrowsiness;
import com.google.android.material.snackbar.Snackbar;

import androidx.appcompat.app.AppCompatActivity;

import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.navigation.NavController;
import androidx.navigation.Navigation;
import androidx.navigation.ui.AppBarConfiguration;
import androidx.navigation.ui.NavigationUI;


public class AddDetialsActivity extends AppCompatActivity {
//    Toast.makeText()
//    SharedPreferences sharedPreferences = getSharedPreferences("MyPreference",MODE_PRIVATE);
//
//    SharedPreferences.Editor myEdit = sharedPreferences.edit();
    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_add_detials);

    }
    public void saveNumber(View v){

        TextView num1 = (TextView) findViewById(R.id.num1) ;
        TextView num2 = (TextView) findViewById(R.id.num2) ;
//        myEdit.putString("num1", num1.toString());
//        myEdit.putString("num2", num1.toString());
//        myEdit.commit();
    }
    public void saveMsg(View V){

        TextView msg = (TextView) findViewById(R.id.emergencymessage) ;
//        myEdit.putString("msg", msg.toString());
//        myEdit.commit();
    }

}