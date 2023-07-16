using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class MovingPlayer : MonoBehaviour
{
    public AudioSource jump;
    public AudioSource coin;
    public AudioSource death1;
    private bool slowmo = false;
    private bool shield = false;
    public bool isdeath = false;
    private float slowmoTime = 0;
    private float shieldTime = 0;
    public Text numberScore;
    public float springForce = 1000f;
    private float score = 0f;
    public ParticleSystem ps;
    public ParticleSystem death;
    private Vector2 direction;
    public Rigidbody2D rb;
    public float moveSpeed = 5f;
    public float jumpForce = 500f;
    public float dashForce = 200f;
    private bool dash = false;
    private Image shieldColor;
    public Button reset;

    void Start()
    {
        Time.timeScale = 1f;
        Button reset = GetComponent<Button>();
        rb = GetComponent<Rigidbody2D>();
        ParticleSystem ps = GetComponent<ParticleSystem>();
        ParticleSystem death = GetComponent<ParticleSystem>();
        GameObject.Find("Circle").GetComponent<Renderer>().enabled = false;
        shieldColor = GameObject.Find("ShieldTimer").GetComponent<Image>();
    }

    void Update()
    {
        numberScore.text = score.ToString();
        direction.x = moveSpeed;
        direction.y = 0;
        if (slowmo)
            slowmoTime += Time.deltaTime * 2;
        if (slowmoTime > 3)
        {
            slowmo = false;
            slowmoTime = 0;
            Time.timeScale = 1f;
        }

        if (shield)
        {
            shieldTime += Time.deltaTime;
            shieldColor.fillAmount = 1 - (shieldTime * 0.25f);
        }
        if (shieldTime > 4)
        {
            shield = false;
            GameObject.Find("Circle").GetComponent<Renderer>().enabled = false;
            shieldColor.fillAmount = 1f;
            shieldTime = 0;
        }
    }

    public void Jump()
    {
        if (dash)
        { 
        rb.AddForce(new Vector2(0f, dashForce));
        dash = false;
        }
    }

    void FixedUpdate()
    {
        if(!isdeath)
        transform.Translate(direction * Time.fixedDeltaTime);
    }

    private void OnCollisionEnter2D(Collision2D col)
    {
        if (col.gameObject.CompareTag("wall"))
        {
            if (moveSpeed > 0)
            {
                ps.transform.position = new Vector2(23.5f, gameObject.transform.position.y);
                ps.transform.rotation = Quaternion.Euler(0, 180, 0);
            }
            else
            {
                ps.transform.position = new Vector2(-23.5f, gameObject.transform.position.y);
                ps.transform.rotation = Quaternion.Euler(0, 0, 0);
            }
            moveSpeed = moveSpeed * -1;
            ps.Play();
        }
        if (col.gameObject.CompareTag("platforms"))
        {
            rb.AddForce(new Vector2(0f, jumpForce));
            dash = true;
            jump.Play();
        }
        if (col.gameObject.CompareTag("spike") && shield == false)
        {
            death.transform.position = gameObject.transform.position;
            death.Play();
            death1.Play();
            isdeath = true;
            reset.transform.position = new Vector3(0f, 0f, 0f);
            GetComponent<Renderer>().enabled = false;
            GameObject.Find("RestartFade").GetComponent<Image>().enabled = true;
            GetComponent<BoxCollider2D>().enabled = false;
        }
        else if(col.gameObject.CompareTag("spike") && shield)
        {
            shieldColor.fillAmount = 1;
            shield = false;
            rb.AddForce(new Vector2(0f, jumpForce));
            GameObject.Find("Circle").GetComponent<Renderer>().enabled = false;
            shieldTime = 0;
 
        }
    }


    private void OnTriggerEnter2D(Collider2D col)
    {
        if (col.gameObject.CompareTag("coin"))
        {
            score++;
            coin.Play();
        }
        if (col.gameObject.CompareTag("spring"))
        {
            rb.velocity = new Vector2(0f, springForce);
            dash = true;
        }
        if (col.gameObject.CompareTag("slowmo"))
        {
            Time.timeScale = 0.5f;
            slowmo = true;
        }
        if (col.gameObject.CompareTag("shield"))
        {
            shield = true;
            GameObject.Find("Circle").GetComponent<Renderer>().enabled = true;
            shieldColor.fillAmount = 1f;
            shieldTime = 0;
        }
    }
}

