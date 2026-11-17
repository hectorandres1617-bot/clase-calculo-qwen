import numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
BG="#0b0f16"; C="#20c4d8"; Y="#ffe600"; O="#e96c28"
def base(w=8,h=5):
    f,a=plt.subplots(figsize=(w,h),dpi=160); f.patch.set_facecolor(BG); a.set_facecolor(BG)
    for s in a.spines.values(): s.set_color("#445"); 
    a.tick_params(colors="#9fb3c8"); a.grid(color="#223",lw=.8); return f,a
# 1) área bajo y=3x²+1 de 0 a 2
f,a=base(); x=np.linspace(0,2.4,300); a.plot(x,3*x**2+1,color=C,lw=3); xs=np.linspace(0,2,200); a.fill_between(xs,3*xs**2+1,color=C,alpha=.35)
a.axvline(2,color=Y,ls="--",lw=1.5); a.set_title("Nivel 1 · Área bajo y = 3x² + 1, de x = 0 a x = 2",color="white",fontsize=13); a.text(.55,3,"Área = 10",color=Y,fontsize=18,weight="bold")
a.set_xlabel("x",color="#9fb3c8"); a.set_ylabel("y",color="#9fb3c8"); f.tight_layout(); f.savefig("capturas/g1-area-bajo-curva.png",facecolor=BG); plt.close(f)
# 2) área entre y=x y y=x² de 0 a 1
f,a=base(); x=np.linspace(-.1,1.15,300); a.plot(x,x,color=Y,lw=3,label="y = x"); a.plot(x,x**2,color=C,lw=3,label="y = x²")
xs=np.linspace(0,1,200); a.fill_between(xs,xs**2,xs,color=O,alpha=.45); a.text(.38,.2,"Área = 1/6 ≈ 0,167",color="white",fontsize=15,weight="bold")
a.plot([0,1],[0,1],"o",color="white"); a.legend(facecolor=BG,labelcolor="white",edgecolor="#445"); a.set_title("Nivel 3 · Área entre dos curvas",color="white",fontsize=13); f.tight_layout(); f.savefig("capturas/g2-area-entre-curvas.png",facecolor=BG); plt.close(f)
# 3) volumen: y=√x girando alrededor del eje x (perfil + discos)
f,a=base(); x=np.linspace(0,4,300); a.plot(x,np.sqrt(x),color=C,lw=3); a.plot(x,-np.sqrt(x),color=C,lw=3)
for xi in np.linspace(.2,3.9,22): r=np.sqrt(xi); a.add_patch(matplotlib.patches.Ellipse((xi,0),.12,2*r,fill=False,ec=Y,lw=1.1,alpha=.8))
a.text(2.0,-2.3,"Volumen = 8π ≈ 25,13",color="white",fontsize=16,weight="bold",ha="center"); a.set_xlim(-.2,4.4); a.set_ylim(-2.7,2.4); a.set_aspect("equal")
a.set_title("Nivel 3 · Sólido de revolución: y = √x girando alrededor del eje x",color="white",fontsize=12); f.tight_layout(); f.savefig("capturas/g3-volumen-discos.png",facecolor=BG); plt.close(f)
# 4) integral impropia 1/x²
f,a=base(); x=np.linspace(1,12,400); a.plot(x,1/x**2,color=C,lw=3); a.fill_between(x,1/x**2,color=C,alpha=.35); a.text(4,.55,"Área desde 1 hasta ∞ = 1\n(aunque la cola es infinita)",color=Y,fontsize=14,weight="bold")
a.set_ylim(0,1.1); a.set_title("Nivel 3 · Integral impropia de 1/x² desde 1",color="white",fontsize=13); f.tight_layout(); f.savefig("capturas/g4-impropia.png",facecolor=BG); plt.close(f)
print("ok")
