import sys, numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
BG="#0b0f16"; C="#20c4d8"; Y="#ffe600"; O="#e96c28"; V="#7a4cff"; W="#ffffff"; G="#9fb3c8"
VERT = len(sys.argv)>2 and sys.argv[2]=="v"; FPS=24
SZ=(10.8,19.2) if VERT else (19.2,10.8)
def fig(proj=None):
    f=plt.figure(figsize=SZ,dpi=100); f.patch.set_facecolor(BG)
    a=f.add_axes([.12 if VERT else .09,.25 if VERT else .27,.80 if VERT else .84,.52 if VERT else .5],projection=proj) if not proj else f.add_axes([.02,.12,.96,.6 if VERT else .66],projection=proj)
    a.set_facecolor(BG); return f,a
def estilo2d(a):
    for s in a.spines.values(): s.set_color("#445")
    a.tick_params(colors=G,labelsize=22 if VERT else 20); a.grid(color="#223",lw=1)
def titulo(f,t,sub):
    f.text(.5,.93 if VERT else .93,t,color=W,fontsize=44 if VERT else 38,ha="center",weight="bold")
    f.text(.5,.885 if VERT else .875,sub,color=C,fontsize=30 if VERT else 26,ha="center")
def pie(f,t,col=Y,y=None):
    y=y or (.09 if VERT else .08)
    return f.text(.5,y,t,color=col,fontsize=46 if VERT else 40,ha="center",weight="bold")
def guardar(an,f,nombre):
    an.save(f"anim/{nombre}{'-v' if VERT else ''}.mp4",writer=FFMpegWriter(fps=FPS,bitrate=6000,extra_args=["-pix_fmt","yuv420p"]),savefig_kwargs={"facecolor":BG}); plt.close(f)
def ease(t): return t*t*(3-2*t)

def riemann():
    f,a=fig(); estilo2d(a); titulo(f,"Integral = suma de rectángulos","Área bajo y = 3x² + 1, de x = 0 a x = 2")
    x=np.linspace(0,2,400); a.plot(x,3*x**2+1,color=C,lw=5); a.set_xlim(-.05,2.1); a.set_ylim(0,14)
    fs=[2,3,4,6,8,12,16,24,32,48,64,100]; HOLD=22; TR=6
    t1=pie(f,""); t0=f.text(.5,.17 if VERT else .165,"",color=W,fontsize=34 if VERT else 30,ha="center")
    pol=[]
    def dib(n):
        for p in pol: p.remove()
        pol.clear(); dx=2/n; xs=np.arange(n)*dx+dx
        for xi in xs: pol.append(a.bar(xi-dx,3*xi**2+1,width=dx,align="edge",color=O,alpha=.55,ec=W,lw=max(.3,2.2/ (n**.5))))
        pol[:]=[p for q in pol for p in q.patches]
        s=sum((3*xi**2+1)*dx for xi in xs); t0.set_text(f"n = {n} rectángulos"); t1.set_text(f"Suma ≈ {s:.3f}".replace(".",","))
    N=len(fs)*HOLD+40
    def fr(k):
        i=min(k//HOLD,len(fs)-1)
        if k>=len(fs)*HOLD: 
            for p in pol: p.remove()
            pol.clear(); a.fill_between(x,3*x**2+1,color=C,alpha=.4); t0.set_text("Con infinitos rectángulos…"); t1.set_text("Integral exacta = 10"); t1.set_color(Y); return
        if k%HOLD==0: dib(fs[i])
    return f,FuncAnimation(f,fr,frames=N,interval=40),"riemann"

def entre():
    f,a=fig(); estilo2d(a); titulo(f,"Área entre dos curvas","y = x  y  y = x²  entre x = 0 y x = 1")
    x=np.linspace(-.05,1.1,300); a.plot(x,x,color=Y,lw=5,label="y = x"); a.plot(x,x**2,color=C,lw=5,label="y = x²"); a.set_xlim(-.05,1.1); a.set_ylim(-.05,1.15)
    a.legend(facecolor=BG,labelcolor=W,edgecolor="#445",fontsize=26,loc="upper left"); t1=pie(f,"Área acumulada = 0,000"); N=170
    st=[]; l=a.axvline(0,color=W,ls="--",lw=2)
    def fr(k):
        s=ease(min(1,k/130)); xs=np.linspace(0,s,max(2,int(200*s))); 
        for p in st: p.remove()
        st.clear(); st.append(a.fill_between(xs,xs**2,xs,color=O,alpha=.6)); l.set_xdata([s,s]); A=s**2/2-s**3/3
        t1.set_text(("Área acumulada = %.3f"%A).replace(".",",")+("   →  1/6" if k>=130 else ""))
        if k>=130: t1.set_color(Y)
    return f,FuncAnimation(f,fr,frames=N,interval=40),"area-entre-curvas"

def volumen():
    f,a=fig("3d"); titulo(f,"Volumen por discos","V = π ∫ x dx   (y = √x, de 0 a 4)" if VERT else "V = π ∫ x dx  (y = √x girando alrededor del eje x, de 0 a 4)")
    a.set_facecolor(BG); a.xaxis.pane.set_facecolor(BG); a.yaxis.pane.set_facecolor(BG); a.zaxis.pane.set_facecolor(BG)
    for ax in (a.xaxis,a.yaxis,a.zaxis): ax.pane.set_edgecolor("#334"); ax._axinfo["grid"]["color"]="#223"; ax.set_tick_params(colors=G,labelsize=14)
    a.set_xlim(0,4); a.set_ylim(-2,2); a.set_zlim(-2,2); a.set_box_aspect((2.2,1,1),zoom=1.3 if not VERT else 0.9); t1=pie(f,"V = 0,00",y=.06); N=260; th=np.linspace(0,2*np.pi,60); sup=[]
    def fr(k):
        s=ease(min(1,k/170))*4
        for p in sup: p.remove()
        sup.clear()
        if s>.01:
            xs=np.linspace(0,s,70); T,X=np.meshgrid(th,xs); R=np.sqrt(X)
            sup.append(a.plot_surface(X,R*np.cos(T),R*np.sin(T),color=C,alpha=.55,lw=0,antialiased=True))
            for xi in np.linspace(0,s,max(2,int(s*7))): 
                sup.append(a.plot(np.full_like(th,xi),np.sqrt(xi)*np.cos(th),np.sqrt(xi)*np.sin(th),color=Y,lw=1.4)[0])
        a.view_init(elev=22,azim=-60+k*(360/N))
        V=np.pi*s**2/2; t1.set_text(("V acumulado = %.2f"%V).replace(".",",")+(" = 8π" if k>=170 else "")); 
        if k>=170: t1.set_color(Y)
    return f,FuncAnimation(f,fr,frames=N,interval=40),"volumen-giro"

def impropia():
    f,a=fig(); estilo2d(a); titulo(f,"Integral impropia","Área bajo 1/x², desde 1 hacia el infinito")
    x=np.linspace(1,20,600); a.plot(x,1/x**2,color=C,lw=5); a.set_xlim(.8,20); a.set_ylim(0,1.1); t1=pie(f,"")
    st=[]; ts=f.text(.5,.17 if VERT else .165,"",color=W,fontsize=34 if VERT else 30,ha="center"); N=160
    def fr(k):
        s=ease(min(1,k/120)); t=1+19*s**2
        for p in st: p.remove()
        st.clear(); xs=np.linspace(1,t,300); st.append(a.fill_between(xs,1/xs**2,color=O,alpha=.55)); ts.set_text(f"hasta t = {t:.1f}".replace(".",","))
        t1.set_text(("Área = %.3f"%(1-1/t)).replace(".",",")+("  → 1" if k>=120 else "")); 
        if k>=120: t1.set_color(Y)
    return f,FuncAnimation(f,fr,frames=N,interval=40),"impropia"

for nombre in sys.argv[1].split(","):
    f,an,n=globals()[nombre](); guardar(an,f,n); print("listo",n,flush=True)
