#pragma once
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class RBT {
private:
	bool deadFLG;
	int age;
	vector<int> pos;
	string color;
	string name;
public:
	RBT(string name, string color, vector<int> pos, int age);
	~RBT();
	void tick();
	bool checkDeath();
	vector<int> move(vector<int>);
	vector<int> getPos();
	string save();
	string getColor();
	string getStr();
};