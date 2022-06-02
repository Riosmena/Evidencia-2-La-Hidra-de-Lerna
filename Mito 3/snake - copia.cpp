#include <windows.h>
#include <iostream>
#include <conio.h>
#include <stdlib.h>

#define ARRIBA		72
#define IZQUIERDA	75
#define DERECHA		77
#define ABAJO		80
#define ESC			27

int cuerpo[200][2];
int n=1;
int tam=2;
int x=10, y=12;
char tecla;
int dir=3;
int xc=30, yc=15;
int velocidad=100;
int punto=0;

void gotoxy(int x, int y){
	HANDLE hCon;
	COORD dwPos;
	
	dwPos.X = x;
	dwPos.Y = y;
	hCon = GetStdHandle(STD_OUTPUT_HANDLE);
	SetConsoleCursorPosition(hCon,dwPos);
}

void pintar(){
	//lineas horizontales
	for(int i=2; i<118; i++){
		gotoxy(i,3); printf("%c",205);
		gotoxy(i,29); printf("%c",205);
	}
	//lineas verticales
	for(int i=4; i<30; i++){
		gotoxy(2,i); printf("%c",186);
		gotoxy(117,i); printf("%c",186);
	}
	//esquinas
	gotoxy(2,3); printf("%c",201);
	gotoxy(2,29); printf("%c",200);
	gotoxy(117,3); printf("%c",187);
	gotoxy(117,29); printf("%c",188);
}

void guardar_posicion(){
	cuerpo[n][0]=x;
	cuerpo[n][1]=y;
	n++;
	if(n==tam) n=1;
}

void pintar_cuerpo(){
	for(int i=1;i<tam;i++){
		gotoxy(cuerpo[i][0],cuerpo[i][1]); printf("*");
	}
}

void borrar_cuerpo(){
	gotoxy(cuerpo[n][0],cuerpo[n][1]); printf(" ");
}

void teclear(){
	
		if(kbhit()){
			tecla=getch();
			switch(tecla){
				case ARRIBA:
					if(dir!=2)
						dir=1;
					break;
				case ABAJO:
					if(dir!=1)
						dir=2;
					break;
				case DERECHA:
					if(dir!=4)
						dir=3;
					break;
				case IZQUIERDA:
					if(dir!=3)
						dir=4;
					break;
			}
		}
	
}

void comida(){
	if(x==xc && y==yc){
		xc=(rand()%112)+4;
		yc=(rand()%21)+4;
		punto++;
		tam++;
		gotoxy(xc,yc);printf("%c",4);
	}
}

bool fin_del_juego(){
	if(y==3 || y==29 || x==2 || x==117) return false;
	for(int j=tam-1; j>0; j--){
		if(cuerpo[j][0]==x && cuerpo[j][1]==y)
			return false;
	}
	return true;
	}

void puntos(){
	gotoxy(3,1); printf("Puntuacion %d", punto);
}

int main(){
	
	pintar();
	gotoxy(xc,yc);printf("%c",4);
	
	while(tecla!=ESC && fin_del_juego()){
		borrar_cuerpo();
		guardar_posicion();
		pintar_cuerpo();
		comida();
		puntos();
		teclear();
		teclear();
		
		if(dir==1) y--;
		if(dir==2) y++;
		if(dir==3) x++;
		if(dir==4) x--;
		
		Sleep(velocidad);	
	}
		
	system("pause>null");
	return 0;
}
