import qrcode
import qrcode.image.svg as svg

def gerar_qr_code(link, nome_arquivo_png='qrcode.png', nome_arquivo_svg='qrcode.svg'):
    if not link.startswith(('http://', 'https://')):
        link = 'https://' + link

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L, 
        box_size=10,
        border=4,
    )

    qr.add_data(link)
    qr.make(fit=True)

    img_png = qr.make_image(fill='black', back_color='white')
    img_png.save(nome_arquivo_png)
    print(f"QR code gerado e salvo como {nome_arquivo_png}")

    img_svg = qrcode.make(link, image_factory=svg.SvgImage)
    with open(nome_arquivo_svg, 'wb') as f:
        img_svg.save(f)
    print(f"QR code gerado e salvo como {nome_arquivo_svg}")

gerar_qr_code('fightclub-dusky.vercel.app')
