# Student Interface

A cross-platform mobile application built with React Native and Expo for students to check in/out for attendance.

## Features

- 📱 **Cross-Platform**: Runs on iOS, Android, and Web
- ✅ **Attendance Check-in**: Students can mark their attendance
- 🔐 **Student Authentication**: Secure login system
- 📊 **Attendance History**: View past attendance records
- 🎨 **Modern UI**: Clean and intuitive interface
- 📍 **Location-based**: Optional location verification

## Tech Stack

- **React Native** - Cross-platform mobile development
- **Expo** - Development platform and toolchain
- **TypeScript** - Type-safe development
- **Expo Router** - File-based navigation
- **React Native Reanimated** - Smooth animations
- **Expo Location** - GPS and location services

## Setup Guide

### Prerequisites

- Node.js 18+ installed
- npm or yarn package manager
- Expo CLI installed globally: `npm install -g @expo/cli`
- For iOS development: Xcode (macOS only)
- For Android development: Android Studio

### Installation

1. **Navigate to the student-interface directory:**
   ```bash
   cd student-interface
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npx expo start
   ```

4. **Run on different platforms:**
   - **iOS Simulator**: Press `i` in the terminal
   - **Android Emulator**: Press `a` in the terminal
   - **Physical Device**: Scan QR code with Expo Go app
   - **Web Browser**: Press `w` in the terminal

### Available Scripts

- `npx expo start` - Start development server
- `npx expo start --ios` - Start and open iOS simulator
- `npx expo start --android` - Start and open Android emulator
- `npx expo start --web` - Start web version
- `npx expo build` - Build for production

### Project Structure

```
app/
├── (tabs)/          # Tab-based navigation
├── _layout.tsx      # Root layout
├── index.tsx        # Home screen
└── global.css       # Global styles

assets/
├── images/          # Image assets
└── fonts/           # Custom fonts
```

### Development Workflow

1. **File-based Routing**: Add new screens by creating files in the `app/` directory
2. **Hot Reload**: Changes are reflected instantly on connected devices
3. **TypeScript**: Full type checking and IntelliSense support
4. **Expo Go**: Test on physical devices without building

### Testing on Devices

#### Physical Devices
1. Install **Expo Go** from App Store (iOS) or Google Play (Android)
2. Scan the QR code from the terminal
3. App will load and update in real-time

#### Simulators/Emulators
- **iOS**: Requires macOS with Xcode installed
- **Android**: Requires Android Studio with AVD setup
- **Web**: Runs in any modern browser

### Building for Production

1. **Configure app.json** with your app details
2. **Build for iOS:**
   ```bash
   npx expo build:ios
   ```
3. **Build for Android:**
   ```bash
   npx expo build:android
   ```

### Environment Setup

Create a `.env` file in the root directory:
```env
EXPO_PUBLIC_API_URL=http://localhost:8000
EXPO_PUBLIC_APP_NAME=Student Attendance
```

### Troubleshooting

- **Metro bundler issues**: Clear cache with `npx expo start --clear`
- **iOS simulator not opening**: Ensure Xcode is installed and updated
- **Android emulator issues**: Check Android Studio AVD configuration
- **Network issues**: Ensure devices are on the same network
