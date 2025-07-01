Auth Signup/ResetPassword form fields
auth_signup.fields

<t name="Auth Signup/ResetPassword form fields" t-name="auth_signup.fields">
    <!-- ANAGRAFICA CANE -->
    <h5 class="mt-4 mb-3">Informazioni sul tuo cane</h5>
    
    <!-- Nome del cane -->
    <div class="mb-3 field-x_studio_dog_name">
        <label for="x_studio_dog_name">Nome del cane</label>
        <input type="text" name="x_studio_dog_name" t-att-value="x_studio_dog_name"
               id="x_studio_dog_name" class="form-control form-control-sm"
               placeholder="es. Fido" required="required"/>
    </div>
    
    <!-- Razza del cane -->
    <div class="mb-3 field-x_studio_dog_breed">
        <label for="x_studio_dog_breed">Razza</label>
        <select name="x_studio_dog_breed" id="x_studio_dog_breed"
                class="form-control form-control-sm" required="required">
            <option value="">-- Seleziona una razza --</option>
            <option value="akita">Akita</option>
            <option value="alano">Alano</option>
            <option value="barboncino">Barboncino</option>
            <option value="bassethound">Basset Hound</option>
            <option value="bassotto">Bassotto</option>
            <option value="beagle">Beagle</option>
            <option value="bergamasco">Pastore Bergamasco</option>
            <option value="bichon">Bichon Frisé</option>
            <option value="border_collie">Border Collie</option>
            <option value="boston_terrier">Boston Terrier</option>
            <option value="boxer">Boxer</option>
            <option value="bracco">Bracco Italiano</option>
            <option value="bulldog_francese">Bulldog Francese</option>
            <option value="bulldog_inglese">Bulldog Inglese</option>
            <option value="bull_terrier">Bull Terrier</option>
            <option value="cane_corso">Cane Corso</option>
            <option value="carlino">Carlino</option>
            <option value="cavalier">Cavalier King Charles Spaniel</option>
            <option value="chihuahua">Chihuahua</option>
            <option value="chow_chow">Chow Chow</option>
            <option value="cocker">Cocker Spaniel</option>
            <option value="collie">Collie</option>
            <option value="dalmata">Dalmata</option>
            <option value="dobermann">Dobermann</option>
            <option value="dogo_argentino">Dogo Argentino</option>
            <option value="golden_retriever">Golden Retriever</option>
            <option value="husky">Siberian Husky</option>
            <option value="jack_russell">Jack Russell Terrier</option>
            <option value="labrador">Labrador Retriever</option>
            <option value="lagotto">Lagotto Romagnolo</option>
            <option value="levriero">Levriero</option>
            <option value="maltese">Maltese</option>
            <option value="maremmano">Pastore Maremmano</option>
            <option value="mastino">Mastino Napoletano</option>
            <option value="meticcio">Meticcio</option>
            <option value="pastore_australiano">Pastore Australiano</option>
            <option value="pastore_tedesco">Pastore Tedesco</option>
            <option value="pechinese">Pechinese</option>
            <option value="pinscher">Pinscher</option>
            <option value="pitbull">Pitbull</option>
            <option value="pointer">Pointer</option>
            <option value="pomerania">Volpino di Pomerania</option>
            <option value="rottweiler">Rottweiler</option>
            <option value="san_bernardo">San Bernardo</option>
            <option value="schnauzer">Schnauzer</option>
            <option value="setter">Setter</option>
            <option value="shar_pei">Shar Pei</option>
            <option value="shiba_inu">Shiba Inu</option>
            <option value="shih_tzu">Shih Tzu</option>
            <option value="spinone">Spinone Italiano</option>
            <option value="springer_spaniel">Springer Spaniel</option>
            <option value="staffordshire">Staffordshire Bull Terrier</option>
            <option value="terranova">Terranova</option>
            <option value="tibetan_terrier">Tibetan Terrier</option>
            <option value="volpino">Volpino Italiano</option>
            <option value="weimaraner">Weimaraner</option>
            <option value="west_highland">West Highland White Terrier</option>
            <option value="yorkshire">Yorkshire Terrier</option>
            <option value="altro">Altra razza</option>
        </select>
    </div>
    
    <!-- Età del cane -->
    <div class="mb-3 field-x_studio_dog_age">
        <label for="x_studio_dog_age">Età (anni)</label>
        <input type="number" name="x_studio_dog_age" t-att-value="x_studio_dog_age"
               id="x_studio_dog_age" class="form-control form-control-sm"
               min="0" max="30" step="1" placeholder="es. 3" required="required"/>
    </div>
    
    <!-- Peso del cane -->
    <div class="mb-3 field-x_studio_dog_weight">
        <label for="x_studio_dog_weight">Peso (kg)</label>
        <input type="number" name="x_studio_dog_weight" t-att-value="x_studio_dog_weight"
               id="x_studio_dog_weight" class="form-control form-control-sm"
               min="0.1" max="100" step="0.1" placeholder="es. 15.5" required="required"/>
    </div>
</t>

		
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	
		
portal_my_details_fields
portal.portal_my_details_fields

<t t-name="portal.portal_my_details_fields">
	<!-- === INFORMAZIONI SUL CANE === -->
	<div class="clearfix"/>
	<h5 class="mt-4 mb-3">Informazioni sul tuo cane</h5>

	<!-- Nome del cane -->
	<div t-attf-class="mb-3 #{error.get('x_studio_dog_name') and 'o_has_error' or ''} col-xl-6">
		<label class="col-form-label" for="x_studio_dog_name">Nome del cane</label>
		<input type="text" name="x_studio_dog_name" t-attf-class="form-control #{error.get('x_studio_dog_name') and 'is-invalid' or ''}" t-att-value="x_studio_dog_name or partner.x_studio_dog_name" placeholder="es. Fido"/>
	</div>

	<!-- Razza del cane -->
	<div t-attf-class="mb-3 #{error.get('x_studio_dog_breed') and 'o_has_error' or ''} col-xl-6">
		<label class="col-form-label" for="x_studio_dog_breed">Razza</label>
		<select name="x_studio_dog_breed" t-attf-class="form-select #{error.get('x_studio_dog_breed') and 'is-invalid' or ''}">
			<option value="">-- Seleziona una razza --</option>
			<option value="akita">Akita</option>
			<option value="alano">Alano</option>
			<option value="barboncino">Barboncino</option>
			<option value="bassethound">Basset Hound</option>
			<option value="bassotto">Bassotto</option>
			<option value="beagle">Beagle</option>
			<option value="bergamasco">Pastore Bergamasco</option>
			<option value="bichon">Bichon Frisé</option>
			<option value="border_collie">Border Collie</option>
			<option value="boston_terrier">Boston Terrier</option>
			<option value="boxer">Boxer</option>
			<option value="bracco">Bracco Italiano</option>
			<option value="bulldog_francese">Bulldog Francese</option>
			<option value="bulldog_inglese">Bulldog Inglese</option>
			<option value="bull_terrier">Bull Terrier</option>
			<option value="cane_corso">Cane Corso</option>
			<option value="carlino">Carlino</option>
			<option value="cavalier">Cavalier King Charles Spaniel</option>
			<option value="chihuahua">Chihuahua</option>
			<option value="chow_chow">Chow Chow</option>
			<option value="cocker">Cocker Spaniel</option>
			<option value="collie">Collie</option>
			<option value="dalmata">Dalmata</option>
			<option value="dobermann">Dobermann</option>
			<option value="dogo_argentino">Dogo Argentino</option>
			<option value="golden_retriever">Golden Retriever</option>
			<option value="husky">Siberian Husky</option>
			<option value="jack_russell">Jack Russell Terrier</option>
			<option value="labrador">Labrador Retriever</option>
			<option value="lagotto">Lagotto Romagnolo</option>
			<option value="levriero">Levriero</option>
			<option value="maltese">Maltese</option>
			<option value="maremmano">Pastore Maremmano</option>
			<option value="mastino">Mastino Napoletano</option>
			<option value="meticcio">Meticcio</option>
			<option value="pastore_australiano">Pastore Australiano</option>
			<option value="pastore_tedesco">Pastore Tedesco</option>
			<option value="pechinese">Pechinese</option>
			<option value="pinscher">Pinscher</option>
			<option value="pitbull">Pitbull</option>
			<option value="pointer">Pointer</option>
			<option value="pomerania">Volpino di Pomerania</option>
			<option value="rottweiler">Rottweiler</option>
			<option value="san_bernardo">San Bernardo</option>
			<option value="schnauzer">Schnauzer</option>
			<option value="setter">Setter</option>
			<option value="shar_pei">Shar Pei</option>
			<option value="shiba_inu">Shiba Inu</option>
			<option value="shih_tzu">Shih Tzu</option>
			<option value="spinone">Spinone Italiano</option>
			<option value="springer_spaniel">Springer Spaniel</option>
			<option value="staffordshire">Staffordshire Bull Terrier</option>
			<option value="terranova">Terranova</option>
			<option value="tibetan_terrier">Tibetan Terrier</option>
			<option value="volpino">Volpino Italiano</option>
			<option value="weimaraner">Weimaraner</option>
			<option value="west_highland">West Highland White Terrier</option>
			<option value="yorkshire">Yorkshire Terrier</option>
			<option value="altro">Altra razza</option>
		</select>
	</div>

	<!-- Età del cane -->
	<div t-attf-class="mb-3 #{error.get('x_studio_dog_age') and 'o_has_error' or ''} col-xl-6">
		<label class="col-form-label" for="x_studio_dog_age">Età (anni)</label>
		<input type="number" name="x_studio_dog_age" t-attf-class="form-control #{error.get('x_studio_dog_age') and 'is-invalid' or ''}" t-att-value="x_studio_dog_age or partner.x_studio_dog_age" min="0" max="30" step="1" placeholder="es. 3"/>
	</div>

	<!-- Peso del cane -->
	<div t-attf-class="mb-3 #{error.get('x_studio_dog_weight') and 'o_has_error' or ''} col-xl-6">
		<label class="col-form-label" for="x_studio_dog_weight">Peso (kg)</label>
		<input type="number" name="x_studio_dog_weight" t-attf-class="form-control #{error.get('x_studio_dog_weight') and 'is-invalid' or ''}" t-att-value="x_studio_dog_weight or partner.x_studio_dog_weight" min="0.1" max="100" step="0.1" placeholder="es. 15.5"/>
	</div>

</t>