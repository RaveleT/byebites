# --- CONTACT & LOCATION FOOTER ---
strlit.markdown(
    """
    <div class="contact-footer">
        <h2 style="margin-bottom: 15px;">Get In Touch With Us</h2>
        <p style="font-size: 1.05rem; margin-bottom: 8px;">
            📧 <b>Email:</b> byebyebite10@gmail.com &nbsp;&nbsp;|&nbsp;&nbsp; 
            📞 <b>Phone:</b> 071 618 0651 &nbsp;&nbsp;|&nbsp;&nbsp; 
            💬 <b>WhatsApp:</b> 060 137 1144
        </p>
        <p style="font-size: 1rem; margin-bottom: 15px;">
            📍 <b>Location:</b> Thohoyandou, University of Venda Main Gate
        </p>
        <hr style="border-color: rgba(255,255,255,0.2); margin: 15px auto; width: 80%;">
        <p style="font-size: 0.85rem; opacity: 0.8;">© 2026 ByeByeBites. All rights reserved. Natural protection you can trust.</p>
    </div>
""",
    unsafe_allow_html=True,
)

# --- TINO LABS / DEVELOPER PROMOTION & QR CODE FOOTER ---
strlit.markdown("<br>", unsafe_allow_html=True)

# Using a balanced 2-column layout for the developer credit
tino_col1, tino_col2 = strlit.columns([1.3, 1])

with tino_col1:
  strlit.markdown(
      """
        <div class="tino-footer" style="text-align: left; height: 100%; display: flex; flex-direction: column; justify-content: center; padding: 25px; margin-top: 0;">
            <h3 style="color: #25D366; margin-bottom: 10px; font-size: 1.4rem;">Want a website or data solution like this?</h3>
            <p style="font-size: 0.95rem; color: #D1D5DB; margin-bottom: 15px; line-height: 1.5;">
                Partner with <b>Tino Labs</b> for custom web applications, professional branding, and automated data workflows tailored to your business.
            </p>
            <p style="font-size: 0.95rem; margin-bottom: 15px;">
                📞 <b>Direct:</b> <a href="https://wa.me/27812678907" style="color: #25D366; text-decoration: none; font-weight: 700;">+27 81 267 8907</a>
            </p>
            <div>
                <a href="https://wa.me/27812678907?text=Hi%20Tino,%20I%20saw%20your%20work%20on%20the%20ByeByeBites%20website%20and%20I'd%20like%20to%20discuss%20a%20project!" target="_blank" class="whatsapp-btn">💬 Chat with Tino Labs</a>
            </div>
        </div>
        """,
      unsafe_allow_html=True,
  )

with tino_col2:
  strlit.markdown(
      """
        <div class="card" style="text-align: center; padding: 15px; border-top: 4px solid #25D366; height: 100%; display: flex; flex-direction: column; justify-content: center;">
            <h4 style="color: #1F2937; margin-bottom: 8px; font-size: 1.1rem;">Scan to Connect</h4>
        """,
      unsafe_allow_html=True,
  )
  qr_img = load_image("Screenshot_20260914_222234_WhatsApp.jpg.jpeg")
  if qr_img:
    strlit.image(qr_img, width=180)
  else:
    strlit.info("WhatsApp QR Code placeholder")
  strlit.markdown(
      '<p style="font-size: 0.8rem; color: #666; margin-top: 8px;">WhatsApp: +27 81 267 8907</p></div>',
      unsafe_allow_html=True,
  )
