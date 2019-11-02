package com.example.hackapp;

import androidx.fragment.app.FragmentActivity;

import android.os.Bundle;
import android.widget.TextView;
import android.widget.Toast;


import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;


import android.os.AsyncTask;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;


public class MapsActivity extends FragmentActivity {

    private static final LatLng PERTH = new LatLng(-31.952854, 115.857342);
    private static final LatLng SYDNEY = new LatLng(-33.87365, 151.20689);
    private static final LatLng BRISBANE = new LatLng(-27.47093, 153.0235);


    private Marker mPerth;
    private Marker mSydney;
    private Marker mBrisbane;

    private GoogleMap mMap;

    OkHttpClient client = new OkHttpClient();

//    @Override
//    protected void onCreate(Bundle savedInstanceState) {
//        super.onCreate(savedInstanceState);
//        setContentView(R.layout.activity_maps);
//
//        SupportMapFragment mapFragment =
//                (SupportMapFragment) getSupportFragmentManager().findFragmentById(R.id.map);
//        mapFragment.getMapAsync(this);
//    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.check_response);
        MediaType mediaType = MediaType.parse("application/x-www-form-urlencoded");
        RequestBody body = RequestBody.create(mediaType, "grant_type=password&scopes=accounts%3Aread%2Ctransactions%3Aread%2Ctransfers%3Awrite%2Caccount%3Awrite%2Cinstitution-users%3Aread%2Crecipients%3Aread%2Crecipients%3Awrite%2Crecipients%3Adelete%2Cdisclosures%3Aread%2Cdisclosures%3Awrite&username=HACKATHONUSER001&password=test123");
        Request request = new Request.Builder()
                .url("http://ncrqe-qe.apigee.net/digitalbanking/oauth2/v1/token")
                .post(body)
                .addHeader("Content-Type", "application/x-www-form-urlencoded")
                .addHeader("Authorization", "Basic NDAxZGFhYjIyZTNiNDAxNjgwZTY4ZTk0NmNiZWI5YzI6MDgxMDBmYjIyYWYzNDBmZGIwZDBjYmNjZTViMGJjMmU=")
                .addHeader("transactionId", "f3df8be7-621d-4278-994a-1f3d6a156c1d")
                .addHeader("institutionId", "DI0516")
                .addHeader("Accept", "application/json")
                .addHeader("Date", "Sat, 02 Nov 2019 07:14:10 GMT")
                .addHeader("User-Agent", "PostmanRuntime/7.19.0")
                .addHeader("Cache-Control", "no-cache")
                .addHeader("Postman-Token", "048b8555-3f60-471f-b2cd-bad0bdfaa644,f9688438-1098-4b0a-b68d-ab05c30085b2")
                .addHeader("Host", "ncrqe-qe.apigee.net")
                .addHeader("Accept-Encoding", "gzip, deflate")
                .addHeader("Content-Length", "278")
                .addHeader("Connection", "keep-alive")
                .addHeader("cache-control", "no-cache")
                .build();
//        new MyAsyncTask1().execute(request);
        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                e.printStackTrace();
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                if (!response.isSuccessful()) {

                } else {
                    try {
                        JSONObject jsonObject = new JSONObject(response.body().string());
                        response.body().close();
                        Request request = new Request.Builder()
                        .url("http://ncrqe-qe.apigee.net/digitalbanking/db-transactions/v1/transactions?accountId=rf5ao6Qclwsth9OfOvUb-EeV1m2BfmTzUEALGLQ3ehU&hostUserId=HACKATHONUSER100")
                        .get()
                        .addHeader("Authorization", "Bearer " + jsonObject.getString("access_token"))
                        .addHeader("transactionId", "fdd1542a-bcfd-439b-a6a1-5a064023b0ce")
                        .addHeader("Accept", "application/json")
                        .build();
                        client.newCall(request).enqueue(new Callback() {
                            @Override
                            public void onFailure(Call call, IOException e) {
                                e.printStackTrace();
                            }

                            @Override
                            public void onResponse(Call call, Response response) throws IOException {
                                JSONObject resObject = null;
                                try {
                                    resObject = new JSONObject(response.body().string());
                                } catch (JSONException e) {
                                    e.printStackTrace();
                                }
                                response.body().close();
                                try {
                                    TextView txt = findViewById(R.id.editText);
                                    String result = resObject.getString("transactions");
                                    txt.setText(result);
                                } catch (JSONException e) {
                                    e.printStackTrace();
                                }
                            }
                        });
                    } catch (JSONException e) {
                        e.printStackTrace();
                    }
                }
            }
        });
    }
//    class MyAsyncTask1 extends AsyncTask<Request, Void, Response> {
//
//        @Override
//        protected Response doInBackground(Request... requests) {
//            Response response = null;
//            try {
//                response = client.newCall(requests[0]).execute();
//
//            } catch (IOException e) {
//                e.printStackTrace();
//            }
//            return response;
//        }
//
//        @Override
//        protected void onPostExecute(Response response) {
//            super.onPostExecute(response);
//            try {
//                //res.setText(response.body().string());
//                //res.setText(response.body().string());
//                JSONObject jsonObject = new JSONObject(response.body().string());
//                response.body().close();
//                Request request = new Request.Builder()
//                        .url("http://ncrqe-qe.apigee.net/digitalbanking/db-transactions/v1/transactions?accountId=rf5ao6Qclwsth9OfOvUb-EeV1m2BfmTzUEALGLQ3ehU&hostUserId=HACKATHONUSER100")
//                        .get()
//                        .addHeader("Authorization", "Bearer " + jsonObject.getString("access_token"))
//                        .addHeader("transactionId", "fdd1542a-bcfd-439b-a6a1-5a064023b0ce")
//                        .addHeader("Accept", "application/json")
//                        .addHeader("User-Agent", "PostmanRuntime/7.19.0")
//                        .addHeader("Cache-Control", "no-cache")
//                        .addHeader("Postman-Token", "f7c195d5-cb19-4c21-9923-f769aa10c0fa,2af1d127-066a-4b59-b7af-88dd09639d50")
//                        .addHeader("Host", "ncrqe-qe.apigee.net")
//                        .addHeader("Accept-Encoding", "gzip, deflate")
//                        .addHeader("Connection", "keep-alive")
//                        .addHeader("cache-control", "no-cache")
//                        .build();
//                new MyAsyncTask2().execute(request);
//            } catch (Exception e) {
//                e.printStackTrace();
//            }
//        }
//    }
//
//    class MyAsyncTask2 extends AsyncTask<Request, Void, Response> {
//
//        @Override
//        protected Response doInBackground(Request... requests) {
//            Response response1 = null;
//            try {
//                response1 = client.newCall(requests[0]).execute();
//            } catch (IOException e) {
//                e.printStackTrace();
//            }
//            return response1;
//        }
//
//        @Override
//        protected void onPostExecute(Response response) {
//            super.onPostExecute(response);
//            try {
//                //res.setText(response.body().string());
//                JSONObject resObject = new JSONObject(response.body().string());
//                response.body().close();
//                res.setText(resObject.toString());
//
//            } catch (Exception e) {
//                //e.printStackTrace();
//                res.setText(e.toString());
//            }
//        }
//    }



//
//    /** Called when the map is ready. */
//    @Override
//    public void onMapReady(GoogleMap map) {
//        mMap = map;
//
//        // Add some markers to the map, and add a data object to each marker.
//        ArrayList<LatLng> cityList = new ArrayList<LatLng>();
//        cityList.add(PERTH);
//        cityList.add(SYDNEY);
//        cityList.add(BRISBANE);
//        creatNewMarkers(cityList);
////        mPerth = mMap.addMarker(new MarkerOptions()
////                .position(PERTH)
////                .title("Perth"));
////        mPerth.setTag(0);
////
////        mSydney = mMap.addMarker(new MarkerOptions()
////                .position(SYDNEY)
////                .title("Sydney"));
////        mSydney.setTag(0);
////
////        mBrisbane = mMap.addMarker(new MarkerOptions()
////                .position(BRISBANE)
////                .title("Brisbane"));
////        mBrisbane.setTag(0);
//
//        // Set a listener for marker click.
//        mMap.setOnMarkerClickListener(this);
//    }
//
//    private void creatNewMarkers(ArrayList<LatLng> citiesList) {
//        Iterator<LatLng> iter  = citiesList.iterator();
//        while (iter.hasNext()) {
//            mPerth = mMap.addMarker(new MarkerOptions()
//                    .position(iter.next())
//                    .title("Perth"));
//            mPerth.setTag(0);
//        }
//    }
//
//
//    /** Called when the user clicks a marker. */
//    @Override
//    public boolean onMarkerClick(final Marker marker) {
//
//        // Retrieve the data from the marker.
//        Integer clickCount = (Integer) marker.getTag();
//
//        // Check if a click count was set, then display the click count.
//        if (clickCount != null) {
//            clickCount = clickCount + 1;
//            marker.setTag(clickCount);
//            Toast.makeText(this,
//                    marker.getTitle() +
//                            " has been clicked " + clickCount + " times.",
//                    Toast.LENGTH_SHORT).show();
//        }
//
//        // Return false to indicate that we have not consumed the event and that we wish
//        // for the default behavior to occur (which is for the camera to move such that the
//        // marker is centered and for the marker's info window to open, if it has one).
//        return false;
//    }
}
