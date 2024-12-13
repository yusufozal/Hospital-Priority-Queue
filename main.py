from flask import Flask, render_template, request, redirect, url_for
import heapq

app = Flask(__name__)


class Hasta:
    def __init__(self, id, oncelik, tedavi_suresi):
        self.id = id
        self.oncelik = oncelik
        self.tedavi_suresi = tedavi_suresi

    def __lt__(self, other):
        return self.oncelik < other.oncelik


class HastaListesi:
    def __init__(self):
        self.hastalar = [
            Hasta(101, 5, 30),
            Hasta(102, 3, 40),
            Hasta(103, 8, 20),
            Hasta(104, 1, 60),
            Hasta(105, 7, 15),
            Hasta(106, 2, 45),
            Hasta(107, 4, 25),
            Hasta(108, 6, 35),
            Hasta(109, 3, 50),
            Hasta(111, 8, 10),
        ]

    def ekle(self, hasta):
        self.hastalar.append(hasta)

    def get_liste(self):
        return self.hastalar


class Hastane:
    def __init__(self):
        self.heap = []
        self.tedavi_edilenler = []
        self.tedavi_edilemeyenler = []

    def min_heap_olustur(self, hasta_listesi):
        for hasta in hasta_listesi:
            heapq.heappush(self.heap, hasta)

    def hasta_ekle(self, yeni_hasta):
        heapq.heappush(self.heap, yeni_hasta)

    def tedavi_simulasyonu(self, toplam_tedavi_suresi):
        mevcut_sure = 0
        while self.heap and mevcut_sure + self.heap[0].tedavi_suresi <= toplam_tedavi_suresi:
            hasta = heapq.heappop(self.heap)
            mevcut_sure += hasta.tedavi_suresi
            self.tedavi_edilenler.append(hasta)

        while self.heap:
            self.tedavi_edilemeyenler.append(heapq.heappop(self.heap))


hastane = Hastane()
hasta_listesi_yoneticisi = HastaListesi()


def format_hasta_listesi(hasta_listesi):
    return [
        {"id": hasta.id, "oncelik": hasta.oncelik, "tedavi_suresi": hasta.tedavi_suresi}
        for hasta in hasta_listesi
    ]


@app.route('/')
def index():
    hasta_listesi = format_hasta_listesi(hasta_listesi_yoneticisi.get_liste())
    return render_template('index.html', hastalar=hasta_listesi)


@app.route('/ekle', methods=['GET', 'POST'])
def hasta_ekle():
    if request.method == 'POST':
        hasta_id = int(request.form['id'])
        oncelik = int(request.form['oncelik'])
        tedavi_suresi = int(request.form['tedavi_suresi'])
        yeni_hasta = Hasta(hasta_id, oncelik, tedavi_suresi)
        hasta_listesi_yoneticisi.ekle(yeni_hasta)
        return redirect(url_for('index'))
    return render_template('ekle.html')


@app.route('/simulasyon')
def tedavi_simulasyonu():
    hastane.heap = []
    hastane.tedavi_edilenler = []
    hastane.tedavi_edilemeyenler = []

    hastane.min_heap_olustur(hasta_listesi_yoneticisi.get_liste())
    hastane.tedavi_simulasyonu(420)
    tedavi_edilen = format_hasta_listesi(hastane.tedavi_edilenler)
    tedavi_edilemeyen = format_hasta_listesi(hastane.tedavi_edilemeyenler)
    toplam_hasta=len(tedavi_edilen)+len(tedavi_edilemeyen)
    return render_template('simulasyon.html', tedavi_edilen=tedavi_edilen, tedavi_edilemeyen=tedavi_edilemeyen,toplam_hasta=toplam_hasta)


if __name__ == '__main__':
    app.run(debug=True)