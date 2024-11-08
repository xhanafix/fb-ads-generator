from src.fb_ad_copy_generator import FBAdCopyGenerator
import pyperclip
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def copy_to_clipboard(text):
    pyperclip.copy(text)
    print("\n✅ Copy dah berjaya disalin ke clipboard!")

def main():
    generator = FBAdCopyGenerator()
    variants = []
    
    while True:
        clear_screen()
        print("\n=== FB Ad Copy Generator (Bahasa Malaysia) ===")
        print("============================================\n")
        
        if not variants:
            print("📝 Sila isi maklumat produk anda:\n")
            
            product_name = input("🏷️ Nama Produk: ")
            print("\n💡 Tips: USP perlu fokus pada benefit utama yang unik")
            usp = input("✨ Unique Selling Point (USP): ")
            
            print("\n🎯 3 Benefit Utama Produk:")
            print("Tips: Tulis dalam ayat yang meyakinkan\n")
            benefit_1 = input("1️⃣ Benefit Pertama: ")
            benefit_2 = input("2️⃣ Benefit Kedua: ")
            benefit_3 = input("3️⃣ Benefit Ketiga: ")
            
            print("\n⚙️ Generating 5 variants of your ad copy...\n")
            variants = generator.generate_ad_copies(
                product_name,
                usp,
                benefit_1,
                benefit_2,
                benefit_3
            )
        
        print("\n=====================================")
        print("📋 5 Variant Copy Iklan Anda:")
        print("=====================================\n")
        
        for i, variant in enumerate(variants, 1):
            print(f"{i}. {variant['name']}")
        
        print("\nPilihan:")
        print("1-5: Pilih variant untuk copy ke clipboard")
        print("R: Jana copy baru (Random)")
        print("N: Buat copy baru dengan produk lain")
        print("Q: Keluar")
        
        choice = input("\nPilihan anda: ").upper()
        
        if choice == 'Q':
            print("\nTerima kasih! Jumpa lagi! 👋")
            break
        elif choice == 'R':
            variants = generator.generate_ad_copies(
                product_name,
                usp,
                benefit_1,
                benefit_2,
                benefit_3
            )
        elif choice == 'N':
            variants = []
            continue
        elif choice.isdigit() and 1 <= int(choice) <= 5:
            variant_idx = int(choice) - 1
            copy_to_clipboard(variants[variant_idx]['content'])
            print(f"\n{variants[variant_idx]['content']}")
            input("\nTekan Enter untuk teruskan...")

if __name__ == "__main__":
    main() 
