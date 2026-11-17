import sys, json, time
from playwright.sync_api import sync_playwright
PREG = {
 "1": "Eres un profesor de matemáticas muy claro. Voy a aprender CÁLCULO INTEGRAL desde cero, de menos a más, en español sencillo. Hoy: NIVEL 1 (lo básico). Explica: 1) qué es una integral con la idea del área bajo una curva, 2) qué es la antiderivada y la constante C, 3) las reglas básicas (potencias, constante, suma, e^x, 1/x, seno y coseno), 4) la integral definida y la regla de Barrow. Da 3 ejemplos resueltos paso a paso, de fácil a un poco más difícil, con fórmulas claras. Termina con 2 ejercicios para practicar. Sé breve y ordenado.",
 "2": "Perfecto. Ahora NIVEL 2 (intermedio): el método de SUSTITUCIÓN (cambio de variable) y el método de INTEGRACIÓN POR PARTES. Para cada método explica cuándo usarlo y da 2 ejemplos resueltos paso a paso (uno con una integral indefinida y uno definida). Termina con 2 ejercicios. Sé breve y ordenado.",
 "3": "Excelente. Ahora NIVEL 3 (aplicaciones y más avanzado): 1) ÁREA ENTRE DOS CURVAS, con el ejemplo y=x y y=x^2 entre sus puntos de corte, 2) VOLUMEN de un sólido de revolución con el método de discos, con el ejemplo y=sqrt(x) entre 0 y 4 girando alrededor del eje x, 3) una breve mención de integrales impropias con un ejemplo. Resuelve cada ejemplo paso a paso y di el resultado numérico. Sé breve y ordenado.",
}
paso = sys.argv[1]
with sync_playwright() as p:
    c=p.chromium.launch_persistent_context("./perfil-navegador",channel="chrome",headless=True,viewport={"width":1400,"height":1000})
    pg=c.pages[0]
    if paso=="1":
        pg.goto("http://127.0.0.1:3030/"); pg.wait_for_timeout(4000)
        pg.get_by_role("button",name="gpt-oss:20b").first.click(); pg.wait_for_timeout(1000); pg.keyboard.type("qwen3.8:27b"); pg.wait_for_timeout(1000)
        pg.get_by_text("qwen3.8:27b").first.click(); pg.wait_for_timeout(1000)
        pg.screenshot(path="capturas/03-modelo-elegido.png")
    else:
        pg.goto(open("url.txt").read().strip()); pg.wait_for_timeout(4000)
    caja=pg.locator("#chat-input"); caja.click(); pg.keyboard.insert_text(PREG[paso]); pg.wait_for_timeout(500)
    pg.screenshot(path=f"capturas/p{paso}-pregunta.png")
    pg.keyboard.press("Enter"); pg.wait_for_timeout(5000)
    if paso=="1": open("url.txt","w").write(pg.url)
    t0=time.time()
    while time.time()-t0<900:
        pg.wait_for_timeout(5000)
        if pg.locator("button[aria-label='Stop'], button:has-text('Detener')").count()==0 and time.time()-t0>15: break
    pg.wait_for_timeout(2000)
    txt=pg.locator(".markdown-prose, .prose").last.inner_text(); open(f"respuesta-{paso}.txt","w").write(txt)
    print("segundos:", int(time.time()-t0), "caracteres:", len(txt))
    # capturas en tramos del último mensaje
    cont=pg.locator("#messages-container"); alto=cont.evaluate("e=>e.scrollHeight"); n=0; y=0
    while y<alto and n<8:
        cont.evaluate(f"e=>e.scrollTo(0,{y})"); pg.wait_for_timeout(600); pg.screenshot(path=f"capturas/p{paso}-resp-{n}.png"); n+=1; y+=800
    print("tramos:", n, "alto:", alto); c.close()
