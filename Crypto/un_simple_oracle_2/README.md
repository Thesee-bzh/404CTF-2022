# Crypto / Un simple oracle [2/2]

## Challenge :star:
Bonjour agent, Suite à votre récente découverte, nous avons pu extraire beaucoup d'informations de ce serveur. Malheureusement, ce service a fermé il y a une semaine, et vient juste de réouvrir après ce qui a été vraisemblablement une mise à jour de sécurité, et il ne semble plus possible d'accéder au secret. Pourriez-vous faire quelque chose?

## Inputs
- server: `challenge.404ctf.fr:30594`

## Solution
Let's see the changes compared to the previous challenge [Un simple oracle [1/2]](../un_simple_oracle_1/README.md):
```console
$ nc challenge.404ctf.fr 30594
Il y a eu quelques petits problèmes lors de ma précédente itération, mais tout a été résolu!
Je peux à nouveau montrer mon secret sans craintes:
5705610017138017672791695476465578006520708025725523712974035715201840897924945897066815526425416863689783797061409989284457922801376369235046802625282936888507074906694292157011911919462788810920365270583954462572819284454282345426301508166705844820894599385463568907121336818206811253071871217798040762416667238092049637388650037847452789703516393551945869233284132697881133895141416405774093905897790018503576774265906783601971807255559335280358601755106488415236855974483460703483692178575383230937822109455800209086049016455363823633158420245353191726100462261694701442972496956666550250307865220464229789570521
Par mesure de sécurité, je ne peux malheureusement plus tout partager ici:
e = 65537

Ceci étant dit, passons à ce que vous vouliez me dire!

>
```

Ok, so the modulus is not given any more... but `e` is still given, as well as the encrypted secret. In fact, in the solution to the first challenge, I didn't even use the modulus ! So same solution applies here, we just have to slighly modify the script when interacting with the server.

```console
[+] Opening connection to challenge.404ctf.fr on port 30594: Done
404CTF{L3_m0dul3_357_t0uj0ur5_7r0uv4bl3}
[*] Closed connection to challenge.404ctf.fr port 30594
```

## Python code
Complete solution in [sol.py](./sol.py)

## Flag
404CTF{L3_m0dul3_357_t0uj0ur5_7r0uv4bl3}
