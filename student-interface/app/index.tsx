import React, { useEffect, useState } from 'react';
import { View, Text, Button, StyleSheet, Alert, Platform, PermissionsAndroid } from 'react-native';

type GeoCoords = {
  latitude: number;
  longitude: number;
  altitude?: number | null;
  accuracy?: number | null;
  altitudeAccuracy?: number | null;
  heading?: number | null;
  speed?: number | null;
};

const CurrentLocation: React.FC = () => {
  const [location, setLocation] = useState<GeoCoords | null>(null);

  // Request location permission for Android
  const requestLocationPermission = async () => {
    if (Platform.OS === 'android') {
      try {
        const granted = await PermissionsAndroid.request(
          PermissionsAndroid.PERMISSIONS.ACCESS_FINE_LOCATION,
          {
            title: 'Location Permission',
            message: 'App needs access to your location',
            buttonNeutral: 'Ask Me Later',
            buttonNegative: 'Cancel',
            buttonPositive: 'OK',
          }
        );
        return granted === PermissionsAndroid.RESULTS.GRANTED;
      } catch (err) {
        console.warn(err);
        return false;
      }
    }
    return true; // iOS permissions handled automatically
  };

  const getLocation = async () => {
    const hasPermission = await requestLocationPermission();
    if (!hasPermission) return;

    // `navigator.geolocation` is available in React Native environments.
    navigator.geolocation.getCurrentPosition(
      (position) => {
        // ensure the coords satisfy GeoCoords
        const coords: GeoCoords = {
          latitude: position.coords.latitude,
          longitude: position.coords.longitude,
          altitude: (position.coords as any).altitude ?? null,
          accuracy: (position.coords as any).accuracy ?? null,
          altitudeAccuracy: (position.coords as any).altitudeAccuracy ?? null,
          heading: (position.coords as any).heading ?? null,
          speed: (position.coords as any).speed ?? null,
        };
        setLocation(coords);
      },
      (error) => Alert.alert('Error', error.message),
      { enableHighAccuracy: true, timeout: 15000, maximumAge: 10000 }
    );
  };

  useEffect(() => {
    getLocation();
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Current Location</Text>
      {location ? (
        <Text>
          Latitude: {location.latitude} {"\n"}
          Longitude: {location.longitude}
        </Text>
      ) : (
        <Text>Fetching location...</Text>
      )}
      <Button title="Refresh Location" onPress={getLocation} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  title: {
    fontSize: 20,
    marginBottom: 20,
    fontWeight: 'bold',
  },
});

export default CurrentLocation;
