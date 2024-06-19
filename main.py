from character import pahlawan, Musuh
from senjata import tongkat_mage, busur_marksman, perisai_tanker, splash, blackshadow
import sys
import time


def main_menu():
    print("=== ⚔️  SELAMAT DATANG DI LEGENDS OF ASWIN ⚔️  ===")
    print("1. Main ▶️")
    print("2. Sejarah Permainan ✨")
    print("3. Keluar ⏩")
    return input("Pilih: ")

def choose_hero():
    print("=== PILIH HERO ===")
    print("1. Mage ❄️")
    print("2. Marksman ⚔️")
    print("3. Tanker ☠️")
    choice = input("Pilih hero: ")
    if choice == '1':
        return pahlawan(nama="Mage", kesehatan=300, senjata=tongkat_mage)
    elif choice == '2':
        return pahlawan(nama="Marksman", kesehatan=350, senjata=busur_marksman)
    elif choice == '3':
        return pahlawan(nama="Tanker", kesehatan=250, senjata=perisai_tanker)
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")
        return choose_hero()

def play_game():
    musuh1 = Musuh(nama="Musuh Biasa", kesehatan=150, senjata=splash)
    musuh2 = Musuh(nama="Raja Terakhir", kesehatan=200, senjata=blackshadow)
    
    pahlawan = choose_hero()
    
    print("Musuh Biasa muncul!")
    while True:
        pahlawan.serangan(musuh1)
        
        if musuh1.kesehatan <= 0:
            print("Anda berhasil mengalahkan Musuh Biasa!")
            input("Tekan Enter untuk melanjutkan...")
            break
        
        if pahlawan.kesehatan > 0:
            musuh1.serangan(pahlawan)
            print(f"⚔️, {musuh1.nama} menyerang {pahlawan.nama} dengan {musuh1.senjata.nama}, menyebabkan {musuh1.senjata.kekuatan} kerusakan ☠️")
            input("Tekan Enter untuk melanjutkan...")

            if pahlawan.kesehatan <= 0:
                print("Anda gagal dalam misi!")
                input("Tekan Enter untuk melanjutkan...")
                return False, pahlawan.nama
            else:
                pahlawan.bar_kesehatan.draw()
                musuh1.bar_kesehatan.draw()
    
    print(" ☠️  Raja Terakhir muncul! ☠️ ")
    while True:
        pahlawan.serangan(musuh2)
        
        if musuh2.kesehatan <= 0:
            print("Anda berhasil mengalahkan Raja Terakhir!")
            input("Tekan Enter untuk melanjutkan...")
            return True, pahlawan.nama
        
        if pahlawan.kesehatan > 0:
            musuh2.serangan(pahlawan)
            print(f"⚔️, {musuh2.nama} menyerang {pahlawan.nama} dengan {musuh2.senjata.nama}, menyebabkan {musuh2.senjata.kekuatan} kerusakan ☠️")
            input("Tekan Enter untuk melanjutkan...")

            if pahlawan.kesehatan <= 0:
                print("Anda gagal dalam misi!")
                input("Tekan Enter untuk melanjutkan...")
                return False, pahlawan.nama
            else:
                pahlawan.bar_kesehatan.draw()
                musuh2.bar_kesehatan.draw()

def display_victory_story(hero_type):
    if hero_type == "Mage":
        print("=== CERITA KEMENANGAN: MAGE ===")
        print("Dengan mengalahkan Raja Terakhir, Mage memperoleh kekuatan leluhur yang legendaris.")
        print("Mage menemukan bahwa kekuatan sihirnya sekarang dipadukan dengan kebijaksanaan dan kekuatan para leluhur.")
        print("Dengan kekuatan baru ini, Mage mampu mengembalikan kedamaian dan keharmonisan ke seluruh dunia Aswin.")
        print("Kekuatan dari tongkat leluhur memungkinkan Mage untuk menjaga dunia dari ancaman jahat di masa depan.")
    elif hero_type == "Marksman":
        print("=== CERITA KEMENANGAN: MARKSMAN ===")
        print("Dengan keahlian dan ketepatannya, Marksman berhasil mengalahkan Raja Terakhir.")
        print("Setelah kemenangan tersebut, Marksman diakui sebagai pahlawan legendaris oleh semua penduduk Aswin.")
        print("Busur Marksman kini memiliki kekuatan magis yang berasal dari diamond emas yang berhasil diamankan.")
        print("Dengan busur magis ini, Marksman menjaga perdamaian dan membasmi kejahatan di seluruh penjuru negeri.")
    elif hero_type == "Tanker":
        print("=== CERITA KEMENANGAN: TANKER ===")
        print("Dengan ketangguhan dan keberaniannya, Tanker berhasil mengalahkan Raja Terakhir.")
        print("Setelah kemenangan ini, perisai Tanker dianugerahi kekuatan magis yang tak tertandingi.")
        print("Tanker sekarang menjadi penjaga utama dunia Aswin, melindungi semua yang lemah dan menjaga kedamaian.")
        print("Kekuatan perisai Tanker mampu menahan serangan apapun, memastikan bahwa dunia tetap aman dari segala ancaman.")

def display_game_history():
    print("=== ⚔️  SEJARAH PERMAINAN ⚔️  ===")
    paragraphs = [
        "Legends of Aswin adalah sebuah permainan petualangan yang mengisahkan perjalanan heroik dalam pencarian diamond emas legendaris, yang diyakini memiliki kekuatan kesaktian yang luar biasa. Permainan ini membawa pemain ke dalam dunia fantasi yang penuh dengan misteri dan tantangan yang menegangkan.",
        
        "Latar Belakang Cerita: Di masa lalu, dunia Aswin adalah tempat yang damai dan makmur. Diamond emas, sebuah artefak magis dengan kekuatan yang tak terhingga, menjadi penjaga keseimbangan dan kedamaian di seluruh negeri. Namun, ketenangan ini tidak berlangsung lama. Kekuatan jahat mulai muncul dan mencoba untuk menguasai diamond emas, yang memicu kekacauan dan pertempuran sengit di seluruh dunia.",
        
        "Misi Pemain: Sebagai seorang pahlawan terpilih, pemain ditugaskan untuk menemukan diamond emas yang hilang dan mengembalikan kedamaian di dunia Aswin. Perjalanan ini bukanlah perjalanan yang mudah. Pemain harus menjelajahi berbagai lokasi yang penuh dengan misteri, dari hutan belantara yang gelap hingga pegunungan yang tertutup salju, dan dari kota-kota kuno yang terlupakan hingga reruntuhan berbahaya yang dipenuhi perangkap.",
        
        "Rintangan dan Musuh: Selama perjalanan, pemain akan menghadapi berbagai rintangan dan musuh yang berusaha menghalangi misi mereka. Mulai dari makhluk mitologis, penyihir jahat, hingga pasukan kegelapan yang dipimpin oleh antagonis utama. Setiap musuh memiliki kekuatan dan strategi yang unik, sehingga pemain harus cerdas dalam memilih senjata dan kemampuan yang tepat untuk melawan mereka."
    ]
    
    for paragraph in paragraphs:
        print_paragraph(paragraph)
        input("Tekan Enter untuk melanjutkan...")
        print()

def print_paragraph(paragraph):
    for char in paragraph:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)  
    print()

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            game_result, hero_type = play_game()
            if game_result:
                display_victory_story(hero_type)
                print("Anda menang!")
            else:
                print("Anda kalah!")
                print("Namun, Anda tetap pahlawan yang kuat!")
        elif choice == '2':
            display_game_history()
        elif choice == '3':
            print("Terima kasih telah bermain!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()