// Cognate Mobile App (React Native)
import React from 'react';
import { SafeAreaView, Text, StyleSheet } from 'react-native';

export default function App() {
  return (
    <SafeAreaView style={styles.container}>
      <Text style={styles.title}>Cognate Mobile</Text>
      <Text>Personalized AI-powered learning on the go!</Text>
      {/* TODO: Add navigation, study scheduling, and peer features */}
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, alignItems: 'center', justifyContent: 'center', backgroundColor: '#f0e6ff' },
  title: { fontSize: 32, fontWeight: 'bold', marginBottom: 16 },
});
